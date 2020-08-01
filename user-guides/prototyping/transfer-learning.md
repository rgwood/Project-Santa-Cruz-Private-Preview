# Transfer learning using Visual Studio Code 

This is a sample showing how to use the Azure Machine Learning SDK and the Azure IoT Edge to do transfer learning using pre-trained TF models. It also shows how to deploy a model to the Project Santa Cruz DevKit in Visual Studio Code.

## Setup Build Environment

1.  Setup Visual Studio Code Development environment.

    **Option 1:**
    
    Install Visual Studio Code, Azure IoT tools, Python, Anaconda, and the Intel Open Vino tool (for the Santa Cruz Vision devkit) using the [Dev Tools Pack Installer](https://go.microsoft.com/fwlink/?linkid=2132187). Documentation for the installer can be found [here](aed-dev-tools-installer.md).<br/>

    **Option 2:**
    *	Install [Visual Studio Code](https://code.visualstudio.com/).
    *	Install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Visual Studio Marketplace. For additional details on installing extensions, see [Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-gallery). The Python extension is named **Python** and published by Microsoft.
    ![Python Extension](user_guides/getting_started/getting_started_images/Python.png)
    * Install [Miniconda with Python 3.7](https://docs.conda.io/en/latest/miniconda.html).
    
Note: If you already have the full Anaconda distribution installed, you don't need to install Miniconda. Alternatively, if you'd prefer not to use Anaconda or Miniconda, you can create a Python virtual environment and install the packages needed for running your AI model development using pip. If you go this route, you will need to install the following packages: pandas, jupyter, seaborn, scikit-learn, keras, and tensorflow.

2.	Launch Visual Studio Code 
3.	Set up a data science environment. 
    1. Begin by creating an Anaconda environment. Open an Anaconda command prompt and run **conda create -n myenv python=3.7 pandas jupyter seaborn scikit-learn keras tensorflow** to create an environment named **myenv**. For additional information about creating and managing Anaconda environments, see the Anaconda documentation.
    2. Next, create a folder in a convenient location to serve as your Visual Studio Code workspace for the tutorial, name it **myworkspace**.
    3. Open the project folder in Visual Studio Code using the **File** > **Open Folder** command.

# Prerequisites

* Azure subscription. If you don't have one, sign up to try the [free or paid version of Azure Machine Learning](https://aka.ms/AMLFree).
* Visual Studio Code. If you don't have it, [install it](https://code.visualstudio.com/docs/setup/setup-overview).
* [Python 3](https://www.python.org/downloads/) (this should be already installed by previous steps).

## Install the Azure IoT and Azure Machine Learning extensions for VS Code to build and deploy AI models to Edge device.

  1. [Azure Machine Learning](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai) ([Azure Account](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai) and the [Microsoft Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) will be automatically installed).
  2. [Azure IoT Hub Toolkit](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)
  3. [Azure IoT Edge](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-edge)
     1. Open Visual Studio Code.
     1. Select the **Extensions** icon from the Activity Bar to open the Extensions view.
     1. In the Extensions view, search for *Azure Machine Learning*.<br/>
     ![Azure Machine Learning](user_guides/getting_started/getting_started_images/azure-machine-learning.png)
     1. Select **Install**.

Repeat the steps above to install remaining extensions.

# Sign in to your Azure Account

In order to provision resources and run workloads on Azure, you have to sign in with your Azure account credentials. To assist with account management, Azure Machine Learning automatically installs the Azure Account extension. Visit the following site to [learn more about the Azure Account extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account).
1.	Open the command palette inVisual Studio Code by selecting **View** > **Command Palette** from the menu bar.
2.	Enter the command "Azure: Sign In" into the command palette to start the sign in process.
3.	Select the **Azure** icon in the Activity Bar.
4.	Select **MACHINE LEARNING**.
5.	Select **Subscription** -> **Your workspace for transfer learning**
6.	Select **Environments** -> **Azure ML Curated Environments** -> **AzureML-TensorFlow** -> **1.12-CPU**
If you are training with GPU, you can use **TensorFlow** -> **1.12-GPU**
7.	Click on **Explorer** in Activity Bar.<br/>
    pip install --upgrade azureml-sdk

The development environment is now setup to start with transfer learning using Visual Studio Code, Python and Jupyter notebooks. 
