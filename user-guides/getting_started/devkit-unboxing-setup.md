# Project Santa Cruz Development Kit unboxing and setup

After [onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) for Private Preview has been completed, and you have received your Project Santa Cruz Development Kit, you are ready to begin developing with Santa Cruz. Reference this guide for information on connecting the devkit components and powering on the device.

## Prerequisites

- [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) for Private Preview has been completed. 
- Project Santa Cruz Devkit.
- Host PC with Wi-Fi capability.

## Devkit unboxing and setup procedure

1. Unbox the devkit components.
    - The devkit contains a carrier board, Azure Eye SoM, Azure Ear SoM, RGB camera, accessories box with required cables, a section of 80/20 1010 Series mounting rail, and a welcome card with a hex key.

    - The major components come mounted to the 80/20 rail out of the box, but they can be removed or adjusted with the included hex key as desired.

1. Connect the devkit components:

    1. Hand screw both WiFi antennas into the carrier board.

    1. Connect the camera to the Azure Eye SoM with the MIPI cable.
    
    1. Connect the Azure Eye SoM to the carrier board with the USB-C cable.

    1. Connect the Azure Ear SoM to the carrier board with the USB Micro Type-B (SoM) to USB-A cable (carrier). 

    1. Connect the power adapter to the carrier board and a wall outlet.

    1. Remove any remaining plastic packaging from the devices.

1. Press the power button on the side of carrier board. Allow some time for the device to boot up. 

1. By default, the devkit will start a SoftAP/Hotspot for initial setup. On your computer, open your network and internet settings and connect to the following:
    1. SoftAP/Hotspot SSID: scz-xxxx    (where xxxx = the last four digits of the devkit's WiFi MAC address)
    2. Password: santacruz
    > [!NOTE]
    > Windows may complain about the SoftAP using a less secure standard (WPA2+TKIP cipher).  This will be addressed in a future build to only allow connections via the CCMP pairwise cipher.

1. The PE-101 carrier board is assigned a default address of 10.1.1.1 on the Santa Cruz Wi-fi AP. To reach the OOBE (out-of-box-experience), open a browser and go to http://10.1.1.1:4242. 

## Next steps

Now that your devkit is powered on and connected to the OOBE, work through the OOBE to connect your devkit to a Wi-Fi network and provision it to your Azure account. For guidance on the OOBE process, please see the [OOBE walkthrough](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md).

