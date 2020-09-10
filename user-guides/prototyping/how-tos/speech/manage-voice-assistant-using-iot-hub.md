# Managing your voice assistant

This article describes how you can configure your voice assistant application using IoT Hub only. 
For a step-by-step tutorial that guides you through the process of creating a voice assistant using demo template, see [QuickStart: Creating a Voice Assistant with the Project Santa Cruz Devkit](../../nocode-speech.md).

1. Open up the [Azure portal](https://portal.azure.com) and find your IoT Hub.
1. Select *IoT Edge* under *Automatic Device Management* in the left navigation menu.
1. Select the device that you wish to configure.
1. Click on **Set Modules**.
1.	Verify that *azureedgedevices* has been added to the container registry credentials. 
   1. Name: *azureedgedevices*
   1. Address: *azureedgedevices.azurecr.io*
   1. User Name: *devkitprivatepreviewpull*

**NOTE:** If you do not have a password for the container registry, please reach to your primary contact for the Santa Cruz private preview program. 

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b

1.	In the IoT Edge Modules section, select azureearspeechclientmodule
 
6.	On Module Settings tab ensure the settings are:
a.	Image URI: azureedgedevices.azurecr.io/azureearspeechclientmodule:preload-devkit
b.	Restart Policy: always
c.	Desired Status: running
7.	No environment variables
8.	Container Create Options
{
    "HostConfig": {
        "Privileged": true,
        "Binds": [
            "/dev:/dev",
            "/var/local:/app/log"
        ]
    }
}
9.	Module Twin Settings: Update the speechConfigs as follows:
All settings can be found in Speech Studio -> Custom Commands -> target project -> Settings
The keyword used below is a default publicly available keyword. If you wish to use your own, you can add your own Custom Keyword by uploading a created table file to Blob Storage that is either anonymous container access or anonymous blob access.
"speechConfigs": {
        "appId": "<Application id for custom command project>",
        "key": "<Speech Resource key for custom command project>",
        "region": "<region your speech studio service is located in. This is likely found in the LUIS resources prediction resource field i.e. westus>",
        "keywordModelUrl": "https://aedspeechscenarios.blob.core.windows.net/keyword-tables/computer.table",
        "keyword": "computer"
    }
10.	Click Update
11.	Next click on the Routes tab at the top and ensure you have a route with the following value:
FROM /messages/modules/azureearspeechclientmodule/outputs/* INTO $upstream
12.	Click Review+Create 
13.	Click Create

A keyword is a word or short phrase which allows your product to be voice activated. For example, "Hey Cortana" is the keyword for the Cortana assistant. Voice activation allows your users to start interacting with your product completely hands-free by simply speaking the keyword. As your product continuously listens for the keyword, all audio is processed locally on the user's device until a detection occurs to ensure their data stays as private as possible. 

