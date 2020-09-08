# Getting started with machine learning development using VS Code + Jupyter Notebooks on AzureML

This article walks you through the process of setting up an Azure Machine Learning workspace, uploading a Jupyter Notebook to the workspace,
creating a compute instance, and running the cells of the notebook within the workspace.

The [notebook](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/Transferlearningusing_SSDLiteV2%20Model.ipynb) performs transfer learning using a pre-trained TensorFlow model (MobileNetSSDV2Lite) on AzureML
in Python with a custom dataset to detect bowls.

The notebook shows how to start from [COCO](https://cocodataset.org/#home), filter it down to only the class of interest (bowls), and then
convert it into the appropriate format. Alternatively, you could use the open-source [VoTT 2](https://github.com/microsoft/VoTT) labeling tool to create
and label bounding boxes in the PASCAL VOC format.

After retraining the model on the custom dataset, the model can then be deployed to your Project Santa Cruz devkit using the module twin update method.
You may then check model inferencing by viewing the live RTSP stream from the Azure Eye SoM of your devkit. Both model retraining and deployment are
performed within the notebook in the cloud.

## Prerequisites

- [Azure Machine Learning Subscription](https://azure.microsoft.com/en-us/free/services/machine-learning/)
- Project Santa Cruz Development Kit with Azure Eye SoM connected
- [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) completed
- [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) completed

## Download Project Santa Cruz GitHub repository

1. Go to the [Project Santa Cruz GitHub repository](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview).
1. Clone the repository or download the ZIP file. Near the top of the screen, click **Code** -> **Download ZIP**.

    ![download_zip](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/download_zip.png)

## Set up Azure Machine Learning portal and notebook

1. Go to the [Azure Machine Learning Portal](https://ml.azure.com).
1. Select your directory, Azure subscription, and Machine Learning workspace from the drop down menus and click **Get started**.

    ![ml_portal_get_started](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/ml_portal_get_started.png)

    If you don’t have an Azure Machine Learning workspace yet, click **Create a new workspace**. In the new browser tab, do the following:

    1. Select your Azure subscription.
    1. Select your resource group.
    1. Enter a name for your workspace.
    1. Select your region.
    1. Select your workspace edition.
    1. Click **Review and create**.
    1. On the next page, review your selections and click **Create**.

        ![workspace_review_and_create](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/workspace_review_and_create.png)

    Please allow a few minutes for workspace creation. After the workspace creation is complete, you will see green check marks next to
    your resources and **Your deployment is complete** at the top of the Machine Learning Services overview page.

    ![workspace_creation_complete](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/workspace_creation_complete.png)

    Once your workspace creation is complete, return to the machine learning portal tab and click **Get started**.

1. In the machine learning workspace homepage, click **Notebooks** on the left-hand pane.

    ![notebooks](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/notebook.png)

1. Under the **My files** tab, click the vertical arrow to upload your .ipynb file.

    ![upload_files](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/upload_files.png)

1. Navigate to and select the [Transferlearningusing_SSDLiteV2 Model.ipynb file](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/Transferlearningusing_SSDLiteV2%20Model.ipynb) from your local copy of the
Project Santa Cruz GitHub repository. Click **Open**. In the **Upload files** window, check the box next
to **I trust contents from this file** and click **Upload**.

    ![select_file](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/select_file.png)

1. On the top right menu bar, check your **Compute** status. If no computes are found, click the **+** icon to create a new compute.

    ![no_computes_found](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/no_computes_found.png)

1. In the **New compute instance** window, enter a **Compute name**, choose a **Virtual machine type**, and select a **Virtual machine size**. Click **Create**.

    ![new_compute_instance](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/new_compute_instance.png)

    Once you click **Create**, your **Compute** status will display a blue circle and **\<your compute name> - Creating**

    ![compute_creating](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/compute_creating.png)

    Your **Compute** status will display a green circle and **\<your compute name> - Running** after compute creation is complete.

    ![compute_running](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/compute_running.png)

1. Once the compute is running, select the **Python 3.6 - AzureML** kernel from the drop-down menu next to the **+** icon.

## Visual Studio Code development environment setup

1. Install the required tools.

    1. Option 1:

        Use the [Dev Tools Pack Installer](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/dev-tools-installer.md) to install the following packages:

        - Visual Studio Code
        - Python 3.5, 3.6, or 3.7
        - Miniconda3
        - Intel OpenVino Toolkit 2020.2

        Note: The Intel OpenVino Toolkit is listed as an optional package in the Dev Tools Pack Installer, but it is required for working
        with the Azure Eye SoM of the Project Santa Cruz Development Kit.

    1. Option 2:

        If you would prefer not to use the Dev Tools Pack Installer, manually install the following packages by clicking the links below and following the specified download and install guidelines:

        - [Visual Studio Code](https://code.visualstudio.com/)
        - [Python 3.5, 3.6, or 3.7](https://www.python.org/)
        - [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)
        - [Intel OpenVino Toolkit 2020.2](https://docs.openvinotoolkit.org/)

    Note: If you already have the full Anaconda distribution installed, you don't need to install Miniconda. Alternatively, if you'd prefer not to use
    Anaconda or Miniconda, you can create a Python virtual environment and install the packages needed for running your AI model development using pip.

1. Launch Visual Studio Code.
1. Set up a data science environment.
    1. There are 2 ways to setup a data science environment
        - Option 1 - Connect to an existing or new machine learning remote compute instance which already has the curated ml packages
        (this is the option we will be using in this tutorial)
        - Option 2 - Setup conda environment on local machine (the tutorial for using local compute instance will be coming soon...)
   	        1. Open an Anaconda or Minianaconda command prompt and run the following command to create an environment
                named **myenv** with the specified packages:
                `conda create -n myenv python=3.7 pandas jupyter seaborn scikit-learn keras tensorflow=1.15`
                For additional information about creating and managing Anaconda environments, see the
                [Anaconda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
            1. Create a folder in a convenient location to serve as your Visual Studio Code workspace. Name it **myworkspace**.
            1. Open **myworkspace** in Visual Studio Code by clicking **File** > **Open Folder** > **Select Folder**.
            1. From explorer, navigate to and select the [Transferlearningusing_SSDLiteV2 Model.ipynbb file](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/Transferlearningusing_SSDLiteV2%20Model.ipynb) from your local copy of the Project Santa Cruz GitHub repository. Copy this notebook file to the myworkspace folder.

## Azure integration with Visual Studio Code

1. If you haven't already, sign up for the [free or paid version of Azure Machine Learning](https://aka.ms/AMLFree).
1. Install the following Azure extensions for VS Code:
    - [Azure Machine Learning extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai)
      (the [Azure Account extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account)
    - Python Insiders extension (via the command Palette: “Python: Switch to Insiders Daily Channel”)
    - [Azure Account extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account)
      Reload your window.
    - [Azure IoT Hub Toolkit extension](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)
    - [Azure IoT Edge extension](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-edge)
1. Sign in to your Azure Account within Visual Studio Code to provision resources and run workloads on Azure.
    1. Open the command palette in Visual Studio Code by selecting **View** > **Command Palette** from the menu bar.
    1. Enter **Azure: Sign In** into the command palette to start the login process.

        ![azure_sign_in](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/transfer_learning_azure_sign_in.png)

    1. Select the **Azure** icon in the Activity Bar.
    1. Activate the Python extension and Azure account by navigating to the Azure tab on the left-hand side of VS Code.
    1. Open Notebook Transferlearningusing_SSDLiteV2 Model_VSCode.ipynb from workspace folder
    1. From View Command Palette, invoke the “Python: specify local or remote Jupyter server for connections” command.
    1. You should see a list of connection options to choose from. Pick the “Azure ML Compute Instances” option.
    1. Follow the guided prompts to choose a subscription, workspace, and running remote compute instance.
       You can choose to create a new compute instance at this point if you wish.
    1. After selecting a compute instance, you’ll be prompted to reload your VS Code window. Once you reload, select
       the **Python 3.6 - AzureML** kernel and you can now run any of the cells in your Notebook.
    1. Running a Notebook cell will instantiate the connection between your Notebook and your
       compute instance. The Notebook toolbar will be updated to reflect the compute instance you’re working on.

## Working with the notebook

You are now ready to run the notebook to train your custom bowl detector in VS Code and deploy it to your devkit. Make sure to run
each cell of the notebook individually as some of the cells require input parameters before executing the script. Cells that require input
parameters may be edited directly in the notebook. To run a cell, click the play icon on the left side of the cell:

![run_cell](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/run_cell1.png)


## Provide feedback

After completing the advanced tools local development experience as well as the [cloud development experience](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks),
please provide feedback on your experience via
this [questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRzoJxrXKT0dEvfQyxsA0h8lUMzE0V0pCTFU4UUVSS0xTRUtNT0hZSEs1Ry4u).
Your feedback will help us continue to fine-tune and improve the advanced tools experience.

For more information on Project Santa Cruz Quests and to provide feedback on other experiences,
please visit the [test scenarios page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/test-scenarios.md).
