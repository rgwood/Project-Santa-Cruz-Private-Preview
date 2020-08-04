<!---
title: USB updating                        # the article title to show on the browser tab
description: Walks a user through the usb update process for the devkit carrier board (July 2020). 
author: elqu20      # the author's GitHub ID - will be auto-populated if set in settings.json
ms.author: v-elqu     # the author's Microsoft alias (if applicable) - will be auto-populated if set in settings.json
ms.date: {@date}           # the date - will be auto-populated when template is first applied
ms.topic: reference  # the type of article
--->
# USB updating   

This guide will show you how to flash the carrier board of the Santa Cruz devkit with a new image file over USB. Ensure all prerequisites are satisfied before working through the USB update procedure.  

## Prerequisites 

- Windows or Linux PC with an available USB Type C port. 

- USB-C cable, included in the Project Santa Cruz Development Kit.  

- Ballpoint pen or small screwdriver. This will be used to toggle the DIP switches of the carrier board.  

- HDMI cable and external monitor for verifying the update.  

- Santa Cruz image flash tool. To download the tool, go to http://projectsantacruz.microsoft.com/update and download the emmc_flashing_tools artifact under the pipelines artifact tab. The artifact contains a README file, the script for UUU, and the flash.bin firmware, which is used to flash the eMMC of the carrier board.  

- [NXP UUU tool](https://github.com/NXPmicro/mfgtools/releases/tag/uuu_1.3.102). Download the uuu.exe file under the Assets tab. Move the .exe file to the emmc_flashing_tools artifact folder and click on the .exe file to install the NXP UUU tool.  

- [7zip](https://www.7-zip.org/). For Windows users, this software will be used for extracting files from an XZ compressed folder. Linux users do not need to install 7zip. Download the appropriate .exe file and click on the .exe file to install the software.  

## USB Update Procedure

1. Go to http://projectsantacruz.microsoft.com/update and download the full devkit image (pe101-<version>.raw.xz).  

1. Extract the pe101-\<version>.raw file from the pe101-\<version>.raw.xz file. To do this, right click on the .xz file and select 7-Zip > Extract Here.  

1. Copy the extracted pe101-\<version>.raw file to the Santa Cruz image flash tool folder.  

1. Power off the carrier board and unplug the power cable. Remove the SD card from the SD card slot.  

1. Using the tip of a ballpoint pen or small screwdriver, toggle DIP switch number 1, 3, and 4 to ON and DIP switch number 2 to OFF (position 1011). This will set the device to USB flash mode.

    ![dip_switches](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/updates/article_images/dip_switches.png)

1. Plug in the carrier board power cable and turn on the device.  

1. Connect the carrier board to the host PC with the USB-C cable.  

1. Open a command prompt (Windows) or a terminal (Linux) and navigate to the Santa Cruz image flash tool folder. Run the following command in Windows: 

    ```console
    C:\Users\user\scz_imageflashtool> uuu.exe -b emmc_full.txt fast-hab-fw.raw pe101-<version>.raw  
    ```

1. Once flashing is complete, power off the carrier board and unplug the power cable. Unplug the USB cable from the PC and the carrier board.  

1. Using the tip of a ballpoint pen or small screwdriver, toggle DIP switch number 3 to OFF  (position 1001). This will set the device to eMMC boot mode.  

1. To verify the update, plug in the carrier board power cable, and connect the carrier board to an external monitor with an HDMI cable. Power on the carrier board. The device should boot to the newly installed image version, and system bootup console logs will be visible on the monitor.  