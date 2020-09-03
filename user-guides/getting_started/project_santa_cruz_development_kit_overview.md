# Project Santa Cruz Development Kit Overview

## Devkit Contents

The Project Santa Cruz Development Kit contains the following major components:

-	Carrier board with Wi-Fi antennas
-	Azure Eye SoM 
-	Azure Ear SoM (includes microphone array)
-	RBG camera (connects to Eye SoM)
-	Required cables: MIPI, USB-C, USB Micro Type-B to USB-A, power cable.
-	Welcome card with hex key
-	Section of 80/20 1010 Series mounting rail

For more detailed specs, please see the datasheets for the [devkit]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/hardware/project_santa_cruz_developer_kit_datasheet.md), [Eye SoM]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/hardware/project_santa_cruz_eye_datasheet.md), and [Ear SoM]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/hardware/project_santa_cruz_ear_datasheet.md).

## Getting Started

There are three main stages to getting started with your Project Santa Cruz Development Kit:

1. [Onboarding]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md)

1. [Devkit unboxing and set up]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/devkit-unboxing-setup.md)

1. [OOBE]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md)

In the [onboarding stage](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md), you will assign an Azure subscription within your account to Project Santa Cruz. The onboarding tool will walk you through the process of creating an IoT Hub within your Azure subscription to use with Project Santa Cruz. You will have the option of enabling services, such as the Device Provisioning Service (DPS), Azure Device Update (ADU), and Automatic Import Updates, within your IoT Hub.

After onboarding has been completed, follow the [devkit unboxing and set up guide](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/devkit-unboxing-setup.md) for guidance on connecting the various components of the kit and powering on your device. 

Once your devkit is powered on, work through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) (out-of-box experience) to connect your devkit to a Wi-Fi network, set up an SSH login (optional), connect your devkit to your Azure account, and assign it to your Project Santa Cruz IoT Hub (created during onboarding).

After the onboarding, devkit set up, and OOBE have been completed, you are ready to begin prototyping. 

## Vision and Speech Experiences

There are a number of no-code vision and audio solutions available for prototyping with your devkit. For more information on these experiences, please reference the [prototyping documentation](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/user-guides/prototyping). 

## Updating your Devkit

Your devkit OS and firmware may be updated over-the-air (OTA) or via USB. For more information on updating your device, please see the [update experience documentation](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/update_experience_overview.md).
