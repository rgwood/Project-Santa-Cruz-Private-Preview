# View your device's inference telemetry

Follow this guide to view your Project Santa Cruz devkit's model inference telemetry.

## Prerequisites

* Project Santa Cruz Development Kit with the Azure Eye SoM connected.

* [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) complete.

* [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) complete.

* [Model deployed](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision-deploy-model.md) to your devkit.

## View telemetry

1. Power on your devkit.

1. Download and install the [Azure IoT Explorer](https://github.com/Azure/azure-iot-explorer/releases). If you are a Windows user, select the .msi file.

    ![azure_iot_explorer_download](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_azure_iot_explorer_download.png)

1. Connect your IoT Hub to the Azure IoT Explorer.

    1. Go to the [Azure Portal](https://ms.portal.azure.com/#home).

    1. Select **All resources**.

        ![azure_portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_azure_portal.png)

    1. Select the IoT Hub that your device is connected to.

        ![iot_hub](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_iot_hub.png)

    1. On the left side of your IoT Hub page, select **Shared access policies**.

        ![shared_access_policies](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_shared_access_policies.png)

    1. Click on **iothubowner**.

        ![iothubowner](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_iothubowner.png)

    1. Click the blue copy icon next to **Connection string—primary key**.

        ![connection_string](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_connection_string.png)

    1. Open the Azure IoT Explorer and click **+ Add connection**.

    1. Paste the connection string into the **Connection string** box on the **Add connection string** window and click **Save**.

        ![add_connection_string](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_add_connection_string.png)

    1. Point the device at an object for model inferencing.

    1. Select **Telemetry**.

    1. Click **Start** to view telemetry events from device.