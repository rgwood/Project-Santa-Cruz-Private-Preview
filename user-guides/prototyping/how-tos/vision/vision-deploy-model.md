# Deploy a vision AI model to a device

Follow this guide to deploy an existing vision model to your Project Santa Cruz devkit.

## Prerequisites

* Project Santa Cruz Development Kit with the Azure Eye SoM connected.

* [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) complete.

* [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) complete.

## Model Deployment

1. Power on your devkit. If your devkit is not connected to a Wi-Fi network, set up a connection through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) before proceeding.

1. Navigate to the [Project Santa Cruz portal](https://go.microsoft.com/fwlink/?linkid=2135819).

1. On the left side of the overview page, click **Devices**.

    ![overview_devices](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_overview_devices.png)

1. Select your devkit from the list.

    ![devices](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_devices.png)

1. On the next page, click **Deploy a sample model** if you would like to deploy one of the pre-trained sample vision models. If you would like to deploy a [custom no-code vision solution](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/create-nocode-vision.md), click **Deploy a Custom Vision project**.

    ![deploy_model](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_deploy_model.png)

1. Select your preferred **Model Iteration**.
1. Finally, click **Deploy model**.
1. To view your model inferencing in action on a live video stream from your devkit, click **View Deployment**.
