# Dev Tools Pack Installer Overview

The Dev Tools Pack Installer is a one-stop solution that installs and configures all of the tools required to develop an Intelligent Edge solution. Please note that if you have already installed any of the software packages listed below, the Dev Tools Pack Installer will reinstall those packages so that your tools are consistent with the Installer software versions.

## Mandatory Tools Installed

* [Visual Studio Code](https://code.visualstudio.com/)
* [Python 3.6 (Windows) or 3.5 (Linux)](https://www.python.org/)
* [Docker 19.03](https://www.docker.com/)
* [PIP3](https://pip.pypa.io/en/stable/user_guide/)
* [TensorFlow 1.13](https://www.tensorflow.org/)
* [Azure Machine Learning SDK 1.1](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py)

## Optional Tools Available for Installation

* [Nvidia DeepStream SDK 5](https://developer.nvidia.com/deepstream-sdk)
* [Intel OpenVino Toolkit 2020.2](https://docs.openvinotoolkit.org/)
* [Lobe.ai](https://lobe.ai/)  
* [Streamlit](https://www.streamlit.io/)
* [Pytorch 1.4.0 (Windows) or 1.2.0 (Linux)](https://pytorch.org/)
* [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)
* [Chainer 5.2](https://chainer.org/)
* [Caffe](https://caffe.berkeleyvision.org/)
* [CUDA Toolkit 10.0.130](https://developer.nvidia.com/cuda-toolkit)
* [Microsoft Cognitive Toolkit 2.5.1](https://www.microsoft.com/en-us/research/product/cognitive-toolkit/?lang=fr_ca)

## Instructions

1. Download the [Dev Tools Pack Installer](https://go.microsoft.com/fwlink/?linkid=2132187).

1. Click on the **Dev-Tools-Pack-Installer \<version>.exe** to open the installation wizard.

1. On the **Install Dev Tools Pack Installer** page, click **View license** to view the license agreements of each software package included in the installer. If you accept the terms in the license agreements, check the box and click **Next**.

    ![license_agreements](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/dev_tools_license_agreements.png)

1. Click on **Privacy Statement** to review the Microsoft Privacy Statement. If you agree to the privacy statement terms and would like to send diagnostic data to Microsoft, select **Yes** and click **Next**. Otherwise, select **No** and click **Next**.

    ![privacy_statement](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/dev_tools_privacy_statement.png)

1. On the **Configure Components** page, select the optional tools you would like to install (the mandatory tools will install by default).

    1. If you are working with the Azure Eye SoM, which is part of the [Project Santa Cruz Development Kit](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/project_santa_cruz_development_kit_overview.md), make sure to install the Intel OpenVino Toolkit and Miniconda3.

    1. If you are working with the Brainbox Development Kit, make sure to install the Nvidia DeepStream SDK and Miniconda3.

    1. Click **Next** to proceed with the installation.

    ![configure_components](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/dev_tools_configure_components.png)

1. After successful installation of all selected components, the wizard proceeds to the **Completing the setup wizard** page. Click **Finish** to exit the installer.

