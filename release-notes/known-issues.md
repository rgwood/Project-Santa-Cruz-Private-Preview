﻿﻿﻿﻿
# **Known Issues**
If you encounter any of these issues it is not necessary to open a bug, as we are aware of them. If you have trouble with any of the work arounds, please open an Issue in GitHub.

|Area|Description of Issue|Workaround|
|:------|:--|:--|
| OOBE | Can’t complete OOBE unless device’s Wifi is configured (Azure login fails). | 1. SSH to the device access point (10.1.1.1) 2. Identify and copy the device ethernet IP address 3. Connect to OOBE using the copied ethernet IP based URL |
| OOBE | Clicking on links in the EULA during OOBE sometimes does not open a new web page. | Copy the link and open it in a separate browser window. |
| WiFi | The hardware button that toggles the Wifi SoftAP on and off sometimes does not work. | Continue to try pressing the button or reboot the device. |
| WiFi | Users may see a message after connecting to WiFI saying "This Wifi network uses an older security standard." | The devkit's hotspot/SoftAP uses the WEP encryption algorithm.  We will be updating this to WPA2 in a future update. |
| No code speech | Creating custom keywords during the no code speech path is not supported within the Azure portal. | Use Speech Studio to [train custom keywords](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/voice-assistant-config.md#create-custom-keyword). |
| No code speech | Users cannot view entire conversation with speech assistant while in the demo app. Only the "completion" responses are visible. Clarifying questions from the speech assistant are not viewable. | Connect speakers or headphones to the Ear SoM to hear the entire conversation. |
| Portal | Only a maximum of 15 devices are displayed in Azure portal. | If possible, delete unused devices. |
| Device update | Containers do not run after an OTA update. | SSH into the device and restart the Iot Edge container with this command `systemctl restart iotedge`. This will restart all containers. |
| Device update | Users may get a message that the update failed, even if it succeeded. | Confirm the device updated by navigating to the Device Twin for the device in IoT Hub. |
| Dev Tools Pack Installer | Optional Caffe install may fail if Docker is not running properly on system. | Make sure Docker is installed and running, then retry Caffe installation. |
| Dev Tools Pack Installer | Optional CUDA install fails on incompatible systems. | Verify system compatibility with CUDA prior to running installer. |







