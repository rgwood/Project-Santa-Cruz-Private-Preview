# Update experience overview

With Project Santa Cruz, you have the option of updating your device OS and firmware over-the-air (OTA) or via USB. To take advantage of OTA updates, Azure Device Update (ADU) must be enabled within your IoT Hub and Azure account associated with Project Santa Cruz. ADU enablement may be done during the [Private Preview onboarding process](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) or at any time within your [Azure account](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) after onboarding has been completed. Additionally, your device must be connected to a Wi-Fi network, which can be set up through the [OOBE (out-of-box experience)](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md). 

However, if your device is not connected to Wi-Fi and/or you elect not to use ADU, your device may still be updated directly over USB. Update files may be downloaded from https://projectsantacruz.microsoft.com/Download. For more information on how to update your devices, please see the following articles:

- [Carrier board (devkit) OS OTA updating](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ota_update.md)

- [Ear SoM firmware OTA updating](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ear_som_firmware.md)

- [Carrier board (devkit) OS USB updating](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/usb_updating.md)
