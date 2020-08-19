<!---
title: Over-the-air (OTA) updating                     # the article title to show on the browser tab
description: Walks a user through the over-the-air (OTA) updating process for Project Santa Cruz Private Preview (July 2020). 
author: elqu20      # the author's GitHub ID - will be auto-populated if set in settings.json
ms.author: v-elqu     # the author's Microsoft alias (if applicable) - will be auto-populated if set in settings.json
ms.date: {@date}           # the date - will be auto-populated when template is first applied
ms.topic: reference  # the type of article
--->
# Over-the-air (OTA) updating

With Project Santa Cruz, you can update your devkit carrier board software over-the-air (OTA) or via [USB](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/usb_updating.md). This guide will walk you through the OTA update process. Prior to executing an OTA update, you must set up an IoT Hub for use with Project Santa Cruz, connect your devkit to a Wi-Fi network, and provision your devkit to your Project Santa Cruz IoT Hub.

## Prerequisites: 

- Host PC.
- Project Santa Cruz Development Kit.
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). 
- [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) complete with ADU enabled. 
- [Devkit setup](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/devkit-unboxing-setup.md) complete.
- [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) complete.
- [General OTA Update Prerequisites](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ota_os_fw_update_prerequisites.md) have been satisfied. 

## OTA Procedure:

1. Plug in and power on your devkit.

1. On your PC, navigate to the [Project Santa Cruz update management website](https://projectsantacruz.microsoft.com/Download). Download the image file (.swu) and manifest file (.json) of your desired update. 

    ![download_update](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_download_update.png)

1. Login to the [Azure Portal](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) (this link allows you to access the Azure Device Update extension, which is a Private Preview service). Click All resources under the Azure services section of the portal homepage. 

    ![azure_services_all_resources](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/firmware_azure_services_all_resources.png)

1. On the All resources page, click on the name of the IoT Hub that was provisioned to your devkit during the OOBE process. 

1. On the left side of the IoT Hub page, click on IoT Edge under Automatic Device Management. On the IoT Edge devices page, find the device ID of your devkit. The status of your device’s Runtime Response should be OK. If an error message is present, resolve the error before proceeding with the OTA update procedure. Click the Device ID of your devkit to open its IoT Edge device page. 

    ![iot_hub](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/firmware_iot_hub.png)

1. On your devkit’s IoT Edge device page, the Runtime Status of all installed modules should be listed as running. 

    ![iot_edge_device_page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_iot_edge_device_page.png)

1. Navigate back to the IoT Hub page and click Import updates under Azure Device Update on the left side of the IoT Hub page. The first time you navigate to Azure Device Update (ADU), you will be asked for your ADU Account Name and Instance Name. These will be provided to you by your Project Santa Cruz representative. Click Import New Update at the top of the Import updates page. 

    ![import_updates](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_import_updates.png)

1. Click on the boxes under Select Import Manifest File and Select Update Files to select the appropriate manifest file (.json) and update file (.swu). Please note that only one update file we be needed for re-imaging the carrier board of your devkit. 

    ![select_update](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_select_update.png)

1. Select the appropriate storage container under Select Storage Container. The storage container list will also provide the option to create a new storage container to use during the OTA update process. After selecting your storage container, click Submit.

    ![select_storage_container](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_select_storage_container.png)

1. Click the Refresh icon at the top of the Import updates page. Once the update files have been imported, the status will display as Succeeded. 

    ![import_success](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_import_success.png)

1. (Optionally) create a device group for your devkit. ADU provides the ability to deploy updates to all compatible devices (in this case, Project Santa Cruz devkits) connected to your IoT Hub or to a select group of compatible devices. If you would like to update a select group of devkits, complete the following steps to create a device group:

    1. On the IoT Hub page, click Device groups under Azure Device Update. Click New at the top of the Device groups page. 

        ![device_groups](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_device_groups.png)

    1. In the Add Group window, enter the group name of your choice under Group Name. 

        ![group_name](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_group_name.png)

    1. Select “microsoft” under the Manufacturer drop-down menu. 

        ![manufacturer](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_manufacturer.png)

    1. Select pe101 (the devkit carrier board model name) under the Model drop-down menu. Check the box next to the devkit device IDs that you want to add to the group. Click Save.  If your devkit is not listed here, verify the device runtime status and runtime response, and refresh the page. 

        ![model](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_model.png)

    1. Navigate back to the Group Management page by clicking Device groups under Azure Device Update. Your new device group should now be listed here. 

        ![group_management](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_group_management.png)

1. Next, navigate back to your devkit’s IoT Edge device page by clicking on IoT Edge under Automatic Device Management and clicking the device ID of your devkit. Click Device Twin at the top of the page.  

    ![device_twin_1](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_device_twin_1.png)

1. On the Device Twin page, note the current software version under swVersion. 

    ![device_twin_2](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_device_twin_2.png)

1. Next, click on Deploy updates under Azure Device Update on the left side of the IoT Hub page. Click the blue triangle under the Available Updates tab corresponding to your devkit device model to open the drop-down menu. Find the correct software version and click Deploy to install the update. 

    ![deploy_updates](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_deploy_updates.png)

1. In the Deploy Update window for your selected update, do the following: 

    1. If you would like to deploy the update to a device group, uncheck “Deploy to all compatible devices” and select the device group created earlier in this procedure under the drop-down menu. If you would like to deploy the update to all compatible devices, check the “Deploy to all compatible devices” box. 

    1. Set Begin date/time and End date/time. During this time period, any device in the target device group (or all compatible devices, if selected) that is brought online will receive the update. Once the time period has been set, click Deploy update. The devkit will reboot automatically.

        ![deploy_settings](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_deploy_settings.png)

1. Navigate back to the Device Twin page (IoT Hub > Automatic Device Management > IoT Edge > Device Twin) for your devkit. TargetVersion will show the update version being installed.

    ![device_twin_target_version](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_device_twin_target_version.png)    

1. After the devkit has rebooted, navigate to the Monitor deployments tab of the Deploy updates page. The Deployment Status of the update will be marked as Completed when the update has finished. 

    ![monitor_deployments](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_monitor_deployments.png)

1. For additional update deployment stats, click on the Deployment Status. 

    ![deployment_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_deployment_status.png)

1. To verify that the correct update was installed, navigate back to the Device Twin page for your devkit (IoT Hub > Automatic Device Management > IoT Edge > Device Twin). swVersion will display the current software, which should match the update that was just installed. 

    ![device_twin_updated](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_device_twin_updated.png)

1. As an additional verification step, SSH into your devkit to check the ADU softwareversion.

    1. First, connect to the devkit's Wi-Fi AP (password = santacruz). 
    
        ![wifi_ap](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_wifi_ap.png)  

    1. Open PuTTY. Enter the following and click Open to SSH into your devkit: 

        1. Host Name: 10.1.1.1 
        1. Port: 22 
        1. Connection Type: SSH 
    
        ![putty](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_putty.png)  

    1. Log in to the PuTTY terminal. If you set up an SSH username and password during the [OOBE]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md), enter those login credentials when prompted. Otherwise, enter the following:  

        1. login as: root 
        1. Password: p@ssw0rd 
        
    1. Enter the following in the PuTTY terminal: 
    
        ```console
        cat /etc/adu-version
        ```

        The terminal will display the current software version, which should match the installed update.

        ![putty_terminal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_putty_terminal.png) 
