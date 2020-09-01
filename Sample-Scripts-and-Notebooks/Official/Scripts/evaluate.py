"""
Script to evaluate a model.

To use this script, first train a model, then export whichever checkpoint you want
to use for evaluation using the scripts/export_frozen_graph.py script.
"""
from PIL import Image
import argparse
import cv2
import importlib.util
import numpy as np
import os
import sys
import tensorflow as tf


def detect_on_image(imgfpath: str, detection_graph, min_threshold: float):
    """
    Detects and displays bounding boxes on a single image.
    """
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # Read in the image and convert from BGR to RGB
            image_np = cv2.resize(cv2.imread(imgfpath), (250, 250))[:,:,::-1]  # pylint: disable=no-member

            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)

            # Extract image tensor
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Extract detection boxes
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

            # Extract detection scores
            scores = detection_graph.get_tensor_by_name('detection_scores:0')

            # Extract detection classes
            classes = detection_graph.get_tensor_by_name('detection_classes:0')

            # Extract number of detections
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            # Actual detection.
            boxes, scores, classes, num_detections = sess.run([boxes, scores, classes, num_detections], feed_dict={image_tensor: image_np_expanded})
            print(f"BOXES (shaped {boxes.shape}):\n{boxes}")
            print(f"SCORES (shaped {scores.shape}):\n{scores}")
            print(f"CLASSES (shaped {classes.shape}):\n{classes}")
            print(f"NDETECTIONS (shaped {num_detections.shape}):\n{num_detections}")

            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=3,
                min_score_thresh=min_threshold
                )
            cv2.imshow("Image", image_np[:,:,::-1])
            cv2.waitKey(0)

def detect_on_all_images_in_directory(imgdpath: str, detection_graph, min_threshold: float):
    """
    Detects and displays bounding boxes on one image at a time.
    """
    for fname in os.listdir(imgdpath):
        fpath = os.path.join(imgdpath, fname)
        detect_on_image(fpath, detection_graph, min_threshold)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=str, help="Path to the frozen graph.")
    parser.add_argument("pbtxt", type=str, help=".pbtxt file for the labels in the dataset.")
    parser.add_argument("modelpath", type=str, help="Path to the root of the Tensorflow Object Detection API repository.")
    parser.add_argument("nclasses", type=int, help="Number of classes the detector was trained on.")
    parser.add_argument("image", type=str, help="Path to the image or image directory.")
    parser.add_argument("--min-threshold", '-m', type=float, default=0.30, help="Threshold IOU needed to display a bounding box.")
    args = parser.parse_args()

    # Sanity check the args
    graphpath = args.graph
    if not os.path.isfile(graphpath):
        print(f"Given a path to a frozen graph, but it does not exist: {graphpath}")
        exit(1)

    pbtxtfpath = args.pbtxt
    if not os.path.isfile(pbtxtfpath):
        print(f".pbtxt file is not a file. Given: {pbtxtfpath}")
        exit(2)

    modeldpath = args.modelpath
    if not os.path.isdir(modeldpath):
        print(f"Model path is not a directory. Given: {modeldpath}")
        exit(3)

    if args.nclasses <= 0:
        print(f"Number of classes given is: {args.nclasses}, but must be greater than zero.")
        exit(4)

    # Abspath everything so we don't have to keep doing it
    graphpath = os.path.abspath(graphpath)
    modeldpath = os.path.abspath(modeldpath)
    pbtxtfpath = os.path.abspath(pbtxtfpath)

    # Set up GPU growth (from TF's website)
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
                logical_gpus = tf.config.experimental.list_logical_devices('GPU')
                print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)

    # Adjust python path
    research = os.path.join(modeldpath, "research")
    if 'PYTHONPATH' in os.environ:
        os.environ['PYTHONPATH'] += ":" + research
    else:
        os.environ['PYTHONPATH'] = research

    sys.path.insert(0, research)

    obj_detection_utils = os.path.join(modeldpath, "research", "object_detection", "utils")
    spec = importlib.util.spec_from_file_location("label_map_util", os.path.join(obj_detection_utils, "label_map_util.py"))
    label_map_util = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(label_map_util)

    spec = importlib.util.spec_from_file_location("visualization_utils", os.path.join(obj_detection_utils, "visualization_utils.py"))
    vis_util = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vis_util)

    # Read the frozen graph
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.io.gfile.GFile(graphpath, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    # Load the categories for visualization in the bounding box labels
    label_map = label_map_util.load_labelmap(pbtxtfpath)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=args.nclasses, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Detect on each image in the directory, or on just the single image
    if os.path.isfile(args.image):
        detect_on_image(args.image, detection_graph, args.min_threshold)
    elif os.path.isdir(args.image):
        detect_on_all_images_in_directory(args.image, detection_graph, args.min_threshold)
    else:
        print(f"Given something I don't understand for image. Should be a file or a directory. Given: {args.image}")
        exit(5)
