# Transfer learning local environment setup with Visual Studio Code

This article walks you through the local environment setup process for transfer learning solution development with Visual Studio Code and Jupyter Notebooks. After completing the steps detailed below, you will be able to get started with the [pre-built TensorFlow model](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/Sample-Scripts-and-Notebooks/MobileNetV2SSDL_Train_vscode) for object detection.

## Visual Studio Code development environment setup

1. Install the required tools.

    1. Option 1:

        Use the [Dev Tools Pack Installer](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/dev-tools-installer.md) to install the following packages:

        - Visual Studio Code
        - Python 3.5, 3.6, or 3.7
        - Miniconda3
        - Intel OpenVino Toolkit 2020.2

        Note: The Intel OpenVino Toolkit is listed as an optional package in the Dev Tools Pack Installer, but it is required for working with the Azure Eye SoM of the Project Santa Cruz Development Kit.

    1. Option 2:

        If you would prefer not to use the Dev Tools Pack Installer, manually install the following packages by clicking the links below and following the specified download and install guidelines:

        - [Visual Studio Code](https://code.visualstudio.com/)
        - [Python 3.5, 3.6, or 3.7](https://www.python.org/)
        - [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)
        - [Intel OpenVino Toolkit 2020.2](https://docs.openvinotoolkit.org/)
  
    Note: If you already have the full Anaconda distribution installed, you don't need to install Miniconda. Alternatively, if you'd prefer not to use Anaconda or Miniconda, you can create a Python virtual environment and install the packages needed for running your AI model development using pip.

1. Launch Visual Studio Code.

1. Set up a data science environment.

    1. Open an Anaconda command prompt and run the following command to create an environment named **myenv** with the specified packages:

        ```console
        conda create -n myenv python=3.7 pandas jupyter seaborn scikit-learn keras tensorflow=1.13
        ```

        For additional information about creating and managing Anaconda environments, see the [Anaconda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

    1. Create a folder in a convenient location to serve as your Visual Studio Code workspace. Name it **myworkspace**.

    1. Open **myworkspace** in Visual Studio Code by clicking **File** > **Open Folder** > **Select Folder**.

## Azure integration with Visual Studio Code

1. If you haven't already, sign up for the [free or paid version of Azure Machine Learning](https://aka.ms/AMLFree).

1. Install the following Azure extensions for VS Code:

    - [Azure Machine Learning extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai) (the [Azure Account extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account) and the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) will be automatically installed as well).
  
    - [Azure IoT Hub Toolkit extension](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)

    - [Azure IoT Edge extension](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-edge)

1. Sign in to your Azure Account within Visual Studio Code to provision resources and run workloads on Azure.

    1. Open the command palette in Visual Studio Code by selecting **View** > **Command Palette** from the menu bar.

    1. Enter **Azure: Sign In** into the command palette to start the login process.

        ![azure_sign_in](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/transfer_learning_azure_sign_in.png)

    1. Select the **Azure** icon in the Activity Bar.

    1. Select **MACHINE LEARNING**.

    1. Select **Subscription** -> Your workspace for transfer learning

    1. Select **Environments** -> **Azure ML Curated Environments** -> **AzureML-TensorFlow** -> **1.12-CPU**

        If you are training with GPU, select **1.12-GPU**

    1. Select **Terminal** -> **New Terminal** to open a terminal within VS Code. Enter the following command to install the Azure ML SDK: 

        ```console
        pip install --upgrade azureml-sdk
        ```

## Next Steps

The development environment is now setup to start transfer learning solution development with Visual Studio Code and Jupyter Notebooks. Next, clone the [Project Santa Cruz Github repository](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview) within the **myworkspace** folder. To get started with transfer learning and object detection with your Project Santa Cruz Development Kit, check out the [pre-built TensorFlow model](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/MobileNetV2SSDL_Training%20on%20VS%20Code%20IDE/Transferlearningusing_SSDLiteV2%20Model_VSCode.ipynb).

# Getting Started
This repo is building Tensorflow Object Detection on AzureML - Azure Machine Learning Service. This repo include Python based AzureML development code.

- Build tensorflow object detection docker image for AzureML with Mobilenetssdv2lite base model
- Generate TF record from Pascal VOC format tagged images. The dataset was labelled using VoTT 2 https://github.com/microsoft/VoTT labeling tool to create and label bounding boxes and export in PASCAL VOC format.
- Run training on remote ML compute node

[Open the notebook](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/MobileNetV2SSDL_Training%20on%20VS%20Code%20IDE/Transferlearningusing_SSDLiteV2%20Model_VSCode.ipynb) in VS code and follow the instructions in the notebook by running each cells to do transfer learning with Tensorflow SSDLiteV2 & SSDV2 Models and deploy the trained model to Azure Eye Devkit
