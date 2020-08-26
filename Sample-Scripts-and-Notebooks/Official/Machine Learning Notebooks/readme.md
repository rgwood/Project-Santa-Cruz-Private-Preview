# Getting started with Jupyter Notebooks in Azure Machine Learning Workspace

## Prerequisites

- [Azure Machine Learning Subscription](https://azure.microsoft.com/en-us/free/services/machine-learning/)

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

    Please allow a few minutes for workspace creation. After the workspace creation is complete, you will see green check marks next to your resources and **Your deployment is complete** at the top of the Machine Learning Services overview page.

    ![workspace_creation_complete](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/article_images/workspace_creation_complete.png)

    Once your workspace creation is complete, return to the machine learning portal tab and click **Get started**.

2.	Select Notebooks from the left-hand pane, then select user files under My files section in the middle-pane and then upload the notebook file (..\Project-Santa-Cruz-Private-Preview-main\Project-Santa-Cruz-Private-Preview-main\Sample-Scripts-and-Notebooks\Official\Machine Learning Notebooks\Transferlearningusing_SSDLiteV2 Model.pynb) that was downloaded and extracted from github. 
3.	Select Transferlearningusing_SSDLiteV2 Model.pynb.
4.	On the right hand pane, if no computes found, create New compute by clicking on … next to “No computes found” text. Provide Compute name, select Virtual machine type and the standard virtual machine size and then click on create. 
5.	Once the compute is created, select Jupyter AML Kernel 3.6 from the drop down list.
6.	Now you are ready to get started with transfer learning using pre-trained tensor flow models (MobileNetSSDV2/MobileNetSSDV2Lite on AzureML. This notebook includes python based AzureML development code.
7.	This notebook does transfer learning using custom dataset to detect dog. The trained model can then be deployed to Azure eye devkit using module twin update method. 
8.	The dataset was labelled using Opensource VoTT 2 https://github.com/microsoft/VoTT labeling tool to create and label bounding boxes and export in PASCAL VOC format. 
9.	Make sure to run each cell individually as some of cells will require input parameters before executing the script. 

## Provide feedback
After completing the advanced tools cloud development experience as well as the [local development experience](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/Sample-Scripts-and-Notebooks/Official/MobileNetV2SSDL_TrainingonVSCodeIDE), please provide feedback on your experience via this [questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRzoJxrXKT0dEvfQyxsA0h8lUMzE0V0pCTFU4UUVSS0xTRUtNT0hZSEs1Ry4u). Your feedback will help us continue to fine-tune and improve the advanced tools experience.

For more information on Project Santa Cruz Quests and to provide feedback on other experiences, please visit the [test scenarios page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/test-scenarios.md).
