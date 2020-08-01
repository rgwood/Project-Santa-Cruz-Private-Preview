<!---
title: Over-the-air (OTA) updating                     # the article title to show on the browser tab
description: Walks a user through the over-the-air (OTA) updating process for Project Santa Cruz Private Preview (July 2020). 
author: elqu20      # the author's GitHub ID - will be auto-populated if set in settings.json
ms.author: v-elqu     # the author's Microsoft alias (if applicable) - will be auto-populated if set in settings.json
ms.date: {@date}           # the date - will be auto-populated when template is first applied
ms.topic: reference  # the type of article
--->
# Over-the-air (OTA) updating

With Project Santa Cruz, you can update your devkit carrier board software over-the-air (OTA) or via [USB](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/usb_updating_july_2020.md). This guide will walk you through the OTA update process. Prior to executing an OTA update, you must set up an IoT Hub for use with Project Santa Cruz, connect your devkit to a Wi-Fi network, and provision your devkit to your Project Santa Cruz IoT Hub.

## Prerequisites: 
-	Host PC.
-	Project Santa Cruz Devkit
-	[Onboarding](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/getting_started/onboarding_july_2020.md) completion.
-	[Devkit setup](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/getting_started/devkit_unboxing_setup_july_2020.md) completion.
-	[OOBE](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/getting_started/oobe_july_2020.md) completion.

## OTA Procedure:
1. Plug in and power on your devkit.

1. On your PC, login to the [Azure Portal](https://ms.portal.azure.com/#home) and click All resources under the Azure services section of the portal homepage. 

    ![azure_services_all_resources](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/firmware_azure_services_all_resources.png)

1. On the All resources page, click on the name of the IoT Hub that was provisioned to your devkit during the OOBE process. 

    ![all_resources](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/firmware_all_resources.png)

1. On the left side of the IoT Hub page, click on IoT Edge under Automatic Device Management. On the IoT Edge devices page, find the device ID of your devkit. The status of your device’s Runtime Response should be OK. If an error message is present, resolve the error before proceeding with the OTA update procedure. Click the Device ID of your devkit to open its IoT Edge device page. 

    ![iot_hub](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/firmware_iot_hub.png)

1. On your devkit’s IoT Edge device page, the Runtime Status of all installed modules should be listed as running. 

    ![iot_edge_device_page](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_iot_edge_device_page.png)

1. Navigate back to the IoT Hub page and click Import updates under Azure Device Update on the left side of the IoT Hub page. Click Import New Update at the top of the Import updates page. 

    ![import_updates](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_import_updates.png)

1. Click on the boxes under Select Import Manifest File and Select Update Files to select the appropriate manifest file (.json) and update file (.swu). Please note that only one update file we be needed for re-imaging the carrier board of your devkit. Next, select the appropriate storage container under Select Storage Container. The storage container list will also provide the option to create a new storage container to use during the OTA update process. Finally, click Submit.

    ![select_update](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_select_update.png)

1. Click the Refresh icon at the top of the Import updates page. Once the update files have been imported, the status will display as Succeeded. 

    ![import_success](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_import_success.png)

1. On the IoT Hub page, click Device groups under Azure Device Update on the left side of the IoT Hub page. Click New at the top of the Device groups page. 

    ![device_groups](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_device_groups.png)

1. In the Add Group window, enter the group name of your choice under Group Name. 

    ![group_name](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_group_name.png)

1. Select “microsoft” under the Manufacturer drop-down menu. 

    ![manufacturer](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_manufacturer.png)

1. Select pe101 (the devkit carrier board model name) under the Model drop-down menu. Check the box next to the devkit device IDs that you want to add to the group. Click Save.  If your devkit is not listed here, verify the device runtime status and runtime response and refresh the page. 

    ![model](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_model.png)

1. Navigate back to the Group Management page by clicking Device groups under Azure Device Update on the left side of the IoT Hub page. Your new device group should now be listed here. 

    ![group_management](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_group_management.png)

1. Navigate back to your devkit’s IoT Edge device page by clicking on IoT Edge under Automatic Device Management on the left side of the IoT Hub page and clicking the device ID of your devkit. Click Device Twin at the top of the page.  

    ![device_twin_1](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_device_twin_1.png)

1. On the Device Twin page, note the current software version under swVersion. 

    ![device_twin_2](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_device_twin_2.png)

1. Next, click on Deploy updates under Azure Device Update on the left side of the IoT Hub page. Click the blue triangle under the Available Updates tab corresponding to your devkit device model to open the drop-down menu. Find the correct software version and click Deploy to install the update. 

    ![deploy_updates](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_deploy.png)

1. In the Deploy Update window for your selected update, uncheck “Deploy to all compatible devices” and select the device group created earlier in this procedure under the drop-down menu. 

    ![target_device_group](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_deploy_target_device_group.png)

1. Set Begin date/time and End date/time. During this time period, any device in the target device group that is brought online will receive the update. Once the time period has been set, click Deploy update. The devkit will reboot automatically.

    ![deploy_time](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_deploy_time.png)

1. After the devkit has rebooted, navigate to the Monitor deployments tab of the Deploy updates page. The Deployment Status of the update will be marked as Completed when the update has finished. 

    ![monitor_deployments](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_monitor_deployments.png)

1. For additional update deployment stats, click on the Deployment Status. 

    ![deployment_status](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/ota_deployment_status.png)

1. To verify that the correct update was installed, navigate back to the Device Twin page for your devkit (IoT Hub > Automatic Device Management > IoT Edge > Device Twin). swVersion will display the current software, which should match the update that was just installed. 
