# Tensorflow Object Detection on AzureML project
This repo is building Tensorflow Object Detection on AzureML - Azure Machine Learning Service. This repo include Python based AzureML development code under development. 

- Build tensorflow object detection docker image for AzureML with Mobilenetssdv2lite base model
- Generate TF record from Pascal VOC format tagged images
- Run training on remote ML compute node

# Getting Started
1. Build tensorflow object detection docker image in VS Code. Launch VS Code -> Go to Terminal and run the below command providing the ACR_NAME
```
docker build --tag <ACR_NAME>.azurecr.io/dw-tf-od:v1 .

```
2. Push to Azure Container Registry
```
docker push <ACR_NAME>.azurecr.io/dw-tf-od:v1

```
3. Run (aml-tf-od-ssdlite - vscode.ipynb) notebook and follow the instruction

# Build and Test
- Compatible with Ubuntu 16.04
- Compatible with Python 3.6, and tensorflow-gpu 1.12.0

# Training process description
- "upload_data" folder should be mounted during the AzureML training process
- "upload_data/work/sample-images.zip" file include Pascal VOC sample images and "pipeline_replace.json" file
- "pipeline_replace.json" file replace Tensorflow Object Detection pipeline config file locate in template folder
- To Trigger Azure DevOps pipeline process, upload compressed file on AzureML Workspace Blob Storage, and then, pass the file location
- For more information, review [Azure ML Service documentation](https://docs.microsoft.com/en-us/azure/machine-learning/service/)
- tensorboard integration, check [this link](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/training-with-deep-learning/tensorboard/tensorboard.ipynb)

# Contribute
Dae Woo Kim, Tony Sampige, Harsha Vishwanath
