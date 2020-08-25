## Getting started with Jupyter Notebooks in Azure Machine Learning Workspace
# Clone Project Santa Cruz Github
Launch https://github.com/microsoft/Project-Santa-Cruz-Private-Preview -> Click Code -> Download zip ->Extract the zip file
 
# Launch Machine Learning Azure Portal https://ml.azure.com 
1.	Select Subscription and Machine Learning Workspace from the drop down and click on Get started. If you don’t have Azure Machine Learning workspace, then create a new workspace. Then re-select that workspace in the previous tab and click on Get started. 
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
