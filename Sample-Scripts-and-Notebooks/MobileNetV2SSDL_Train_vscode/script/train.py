import sys
import os
import io
import shutil
import argparse
import math

import zipfile
import logging
import logging.config, os, yaml

import json
import subprocess

import glob
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
import tensorflow as tf
from azureml.core import Experiment

from os import listdir
from os.path import isfile, join
from shutil import copyfile
from PIL import Image

os.chdir('/tensorflow/models/research')
print('pythonpath info : ', sys.path)

if "/tensorflow/models/research" not in sys.path:
    sys.path.append("/tensorflow/models/research")
if "/tensorflow/models/research/slim" not in sys.path:
    sys.path.append("/tensorflow/models/research/slim")
print('path added!')
print('pythonpath info : ', sys.path)

print('system python version : ', sys.version)
print('current dir : ', os.listdir())
print('sys ver : ', sys.executable)

from object_detection.utils import dataset_util
from object_detection.utils import label_map_util
from collections import namedtuple, OrderedDict

loggingConfigPath = 'logging.yaml'
if os.path.exists(loggingConfigPath):
    with open(loggingConfigPath, 'rt') as f:
        loggingConfig = yaml.load(f.read())
        logging.config.dictConfig(loggingConfig)
else:
    logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='dw tf od params')
parser.add_argument('-d','--data_folder', help='Data folder name', required=True)
args = parser.parse_args()

print(os.getcwd()) 
mount_data_folder = args.data_folder

print('mounted dir : ', mount_data_folder)
print('mount dir list : ', os.listdir(mount_data_folder))


# tf-record convert global values
tf_root_folder = '/tensorflow/models/research'
zip_image_path = os.path.join(mount_data_folder, 'tfdata', 'work', 'sample-images.zip')
extract_image_path = '/tensorflow/models/research/tfdata'

tf_checkpoint_dir = os.environ["AZ_BATCHAI_OUTPUT_outputs"]
print(tf_checkpoint_dir)
pascal_image_path = '/tensorflow/models/research/tfdata'
file_split_ratio = 0.80
tf_train_filename = 'train.record'
tf_test_filename = 'test.record'
label_map_path = os.path.join(extract_image_path, 'pascal_label_map.pbtxt')

# replace config global params
json_replace_pipeline_file_path = os.path.join(extract_image_path, 'pipeline_replace.json')
tf_pipeline_config_template_file_path = os.path.join(mount_data_folder, 'tfdata', 'templates', 'pipeline_configs', 'pipeline.config')
tf_pipeline_config_work_file_path = os.path.join(extract_image_path, 'pipeline.config')
#tf_checkpoint_dir = os.path.join(extract_image_path, 'checkpoint')

#tf_checkpoint_dir = os.path.join(model_path, 'checkpoint')
print (tf_checkpoint_dir)

# python unzip processing
def aml_unzip(zip_image_path, extract_image_path):
    zip_ref = zipfile.ZipFile(zip_image_path, 'r')  # parameter path
    zip_ref.extractall(extract_image_path)
    zip_ref.close()
    logging.info('unzip done!')

# convert to tfrecord
def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        base = os.path.basename(xml_file)
        realname = os.path.splitext(base)[0]
        logging.info('file porcessing : %s', realname)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            bb = member.findall('bndbox')[0]
            value = (realname,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(bb.findall('xmin')[0].text),
                     int(bb.findall('ymin')[0].text),
                     int(bb.findall('xmax')[0].text),
                     int(bb.findall('ymax')[0].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def convert_csv(pascal_image_path):
    #image_path = os.path.join(os.getcwd(), 'Annotations')
    image_path = os.path.join(pascal_image_path, 'Annotations')
    csv_df = xml_to_csv(image_path)
    logging.info('Successfully converted xml to csv.')
    return(csv_df)

def split_csv(csv_df, file_split_ratio):
    np.random.seed(1)
    full_labels = csv_df
    
    grouped = full_labels.groupby('filename')
    grouped.apply(lambda x: len(x)).value_counts()

    gb = full_labels.groupby('filename')
    grouped_list = [gb.get_group(x) for x in gb.groups]
    file_count = len(grouped_list)
    file_split = 0.80
    split_index = int(np.floor(file_count * file_split))
    train_index = np.random.choice(file_count, size=split_index, replace=False)
    test_index = np.setdiff1d(list(range(file_count)), train_index)
    train = pd.concat([grouped_list[i] for i in train_index])
    test = pd.concat([grouped_list[i] for i in test_index])

    return train, test

# generate tfrecord
def class_text_to_int(row_label):
    label_map_dict = label_map_util.get_label_map_dict(label_map_path)
    return label_map_dict[row_label]

def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename+'.jpg')), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example

def gen_tf_record(filename, df):
    output_file_path = os.path.join(pascal_image_path, filename)
    writer = tf.python_io.TFRecordWriter(output_file_path)
    path = os.path.join(pascal_image_path, 'JPEGImages')
    examples = df
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = output_file_path
    print('Successfully created the ' + filename + ' TFRecords: {}'.format(output_file_path))

# Load json config file
def json2obj(data): 
    fo = open(data).read()
    return json.loads(fo)

# replace config values function
def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


# unzip image file
aml_unzip(zip_image_path, extract_image_path)

# convert to csv
csv_df = convert_csv(pascal_image_path)
csv_df.head()

# Split df
train_df, test_df = split_csv(csv_df, file_split_ratio)

# generate tfrecord
gen_tf_record(tf_train_filename, train_df)
gen_tf_record(tf_test_filename, test_df)

# config value replace start here
copyfile(tf_pipeline_config_template_file_path, tf_pipeline_config_work_file_path)

# load json object
obj = json2obj(json_replace_pipeline_file_path)

#replace from json data
for key in obj:
    val = obj[key]
    inplace_change(tf_pipeline_config_work_file_path, key, val)
    print("%s : %s" % (key, val))

    
#build slim
res = subprocess.Popen(['python','setup.py', 'build'], stdout=subprocess.PIPE, cwd=os.path.join(tf_root_folder, 'slim'))
res = subprocess.Popen(['python','setup.py', 'install'], stdout=subprocess.PIPE, cwd=os.path.join(tf_root_folder, 'slim'))
print(res.communicate())

#subprocess train.py
res = subprocess.Popen(['python','object_detection/legacy/train.py', '--logtostderr', '--pipeline_config_path=' + tf_pipeline_config_work_file_path, '--train_dir=' + tf_checkpoint_dir], stdout=subprocess.PIPE, cwd=tf_root_folder)
print(res.communicate())

logging.info('train done!')

#subprocess eval.py
res = subprocess.Popen(['python','object_detection/legacy/eval.py', '--logtostderr', '--pipeline_config_path=' + tf_pipeline_config_work_file_path, '--checkpoint_dir=' + tf_checkpoint_dir, '--eval_dir=' + tf_checkpoint_dir], stdout=subprocess.PIPE, cwd=tf_root_folder)
print(res.communicate())

logging.info('eval done!')

#subprocess export_inference_graph.py
logging.info('Start frozen - export inference graph!')
res = subprocess.Popen(['python','object_detection/export_inference_graph.py', '--input_type image_tensor', '--pipeline_config_path=' + tf_pipeline_config_work_file_path, '--trained_checkpoint_prefix=' + os.path.join(tf_checkpoint_dir, 'model.ckpt-10'), '--output_directory=' + os.path.join(tf_checkpoint_dir, 'frozen_model')], stdout=subprocess.PIPE, cwd=tf_root_folder)
#res = subprocess.Popen(['python','object_detection/export_tflite_ssd_graph.py', '--input_type image_tensor', '--pipeline_config_path=' + tf_pipeline_config_work_file_path, '--trained_checkpoint_prefix=' + os.path.join(tf_checkpoint_dir, 'model.ckpt-10'), '--output_directory=' + os.path.join(tf_checkpoint_dir, 'frozen_model')], stdout=subprocess.PIPE, cwd=tf_root_folder)

print(res.communicate())

logging.info('frozen done!')

onlyfiles = [f for f in listdir(os.path.join(tf_checkpoint_dir, 'frozen_model'))]
logging.info('frozen_model folder files %s', onlyfiles)
