# Getting started with advanced development in the cloud via Jupyter Notebooks and Azure Machine Learning

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

## Working with the notebook

You are now ready to run the notebook to train your custom bowl detector and deploy it to your devkit. Make sure to run each cell of the notebook
individually as some of the cells require input parameters before executing the script. Cells that require input parameters may be
edited directly in the notebook. To run a cell, click the play icon on the left side of the cell:

![run_cell](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/run_cell.png)

## Provide feedback

After completing the advanced tools cloud development experience as well as the [local development experience](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/Sample-Scripts-and-Notebooks/Official/MobileNetV2SSDL_TrainingonVSCodeIDE), please provide feedback
via this [questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRzoJxrXKT0dEvfQyxsA0h8lUMzE0V0pCTFU4UUVSS0xTRUtNT0hZSEs1Ry4u).
Your feedback will help us continue to fine-tune and improve the advanced tools experience.

For more information on Project Santa Cruz Quests and to provide feedback on other experiences,
please visit the [test scenarios page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/test-scenarios.md).
