#FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04
#FROM mcr.microsoft.com/azureml/o16n-sample-user-base/ubuntu-miniconda:latest

#https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/training-with-deep-learning/distributed-cntk-with-custom-docker/distributed-cntk-with-custom-docker.ipynb
#GPU base image - microsoft/mmlspark:gpu-0.12
#CPU base image - microsoft/mmlspark:0.12
FROM microsoft/mmlspark:gpu-0.12


# Taken from https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/tools/docker/Dockerfile.gpu
# https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/dockerfiles/android/Dockerfile
LABEL maintainer="dw-aml-tf-od"

ENV CI_BUILD_PYTHON python3


USER root  
# error w/ non-root - mmlspark docker base image issue
RUN mkdir -p /tensorflow
#RUN chown newuser /tensorflow


# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        wget \
        git \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        protobuf-compiler \
        python3 \
        python3-dev \
        rsync \
        software-properties-common \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

COPY . /
RUN pip --no-cache-dir install -r /requirements.txt

# change to tensorflow dir
WORKDIR /tensorflow

# clone the models repo
# RUN git clone https://github.com/tensorflow/models.git
# change to clone specific version
RUN git clone --single-branch --branch r1.13.0 https://github.com/tensorflow/models.git

WORKDIR /tensorflow/models/research

RUN git clone https://github.com/cocodataset/cocoapi.git
RUN cd cocoapi/PythonAPI && \
    make -j8 && \
    cp -r pycocotools /tensorflow/models/research/ && \
    cd ../../ && \
    rm -rf cocoapi

WORKDIR /tensorflow/models/research

RUN wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
RUN unzip protobuf.zip
RUN ./bin/protoc object_detection/protos/*.proto --python_out=.

# Pretrained model
RUN curl -O "http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz" && \
    tar xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz && \
    rm ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz

RUN echo "export PYTHONPATH=${PYTHONPATH}:`pwd`:`pwd`/slim" >> ~/.bashrc

RUN echo "cd /tensorflow/models/research" >> ~/.bashrc

# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# Add work dir
RUN mkdir -p /tensorflow/models/research/tfdata/checkpoint
RUN mkdir -p /tensorflow/models/research/tfdata/checkpoint/frozen_model

# replace eval.py process error  
RUN sed -i -e 's/category_name = unicode(category_name/category_name = str(category_name/g' object_detection/utils/object_detection_evaluation.py

CMD ["/bin/bash"]

