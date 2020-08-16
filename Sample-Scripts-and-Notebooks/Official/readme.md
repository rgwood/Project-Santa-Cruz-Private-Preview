# Getting started with Jupyter Notebooks in Azure Setup a NotebookVM in Azure Machine Learning Workspace.

If you have an Azure Machine Learning service workspace, skip to step #2. Otherwise, create one now.

Sign in to the Azure portal by using the credentials for the Azure subscription you use. In the upper-left corner of the portal, select Create a resource. In the search bar, enter Machine Learning. Select the Machine Learning service workspace search result. In the ML service workspace pane, scroll to the bottom and select Create to begin. In the ML service workspace pane, configure your workspace and select Create. It can take a few minutes to create the workspace. When the process is finished, a deployment success message appears. It's also present in the notifications section. To view the new workspace, select Go to resource. Create a cloud-based notebook server.

Open your Machine Learning workspace in the Azure portal. On your workspace page in the Azure portal, select Notebook VMs on the left. Select +New to create a notebook VM. Provide a name for your VM and select Create. Wait approximately 4-5 minutes until the status changes to Running Launch the Jupyter wed interface in your Notebook VM

Select Jupyter in the URI column for your VM. On the Jupyter notebook webpage, the top foldername is your username. More details about quickstart setup instructions are located here.

Clone this repo to your Notebook VM From the Notebook VM launch the Jupyter web interface as descriped in step #3 above. Click New -> Terminal on the upper right corner of the web interface. You will get a new browser tab with the bash prompt. You can use regular git clone --recursive https://github.com/microsoft/Project-Santa-Cruz-Private-Preview command line commands to clone this repository into a desired folder.

Important update jupyter in the Notebook VM: (this is a temporary step)
pip install –upgrade notebook
sudo -i systemctl restart jupyter

Select a notebook in Official folder to run thru the transfer learning on Azure ML. Set the kernel to Python 3.6 - AzureML.

Refer to the readme.md section for each of the notebook folder which has instructions on how to run the AI model training.

Also find other quickstarts and how-tos on the official documentation site for Azure Machine Learning service.

# Get Started
This repo is building Tensorflow Object Detection on AzureML - Azure Machine Learning Service. This repo include Python based AzureML development code.

Build tensorflow object detection docker image for AzureML with Mobilenetssdv2lite base model
Generate TF record from Pascal VOC format tagged images
Run training on remote ML compute node
