# Managing your voice assistant uing IoT Hub

This article describes how you can configure your voice assistant application using IoT Hub only. 
For a step-by-step tutorial that guides you through the process of creating a voice assistant using demo template, see [QuickStart: Creating a Voice Assistant with the Project Santa Cruz Devkit](../../nocode-speech.md).

1. Open up the [Azure portal](https://portal.azure.com) and find your IoT Hub.
1. Select **IoT Edge** under **Automatic Device Management** in the left navigation menu.
1. Select the device that you wish to configure.
1. Click on **Set Modules**.
1. Verify that the following entry is present in the container registry credentials. Add credential is required.

Name|Address|Username|Password
----|-------|--------|--------
azureedgedevices|azureedgedevices.azurecr.io|devkitprivatepreviewpull|***


**NOTE:** If you do not have a password for the container registry, please reach to your primary contact for the Santa Cruz private preview program. 

6.	In the **IoT Edge Modules** section, select **azureearspeechclientmodule**.
7.	Click on the **Module Settings** tab. Verify configuration.

Image URI|Restart Policy|Desired Status
---------|--------------|--------------
azureedgedevices.azurecr.io/azureearspeechclientmodule:preload-devkit |always|running

8.	Click on the **Environment Variables** tab. Verify that there are no environment variables defined.
9.	Click on the **Container Create Options** tab.

```
    {
        "HostConfig": {
            "Privileged": true,
            "Binds": [
                "/dev:/dev"
            ]
        }
    }
```

10. Click on the **Module Twin Settings** tab. Update the *speechConfigs* section as follows:

```
    "speechConfigs": {
        "appId": "<Application id for custom command project>",
        "key": "<Speech Resource key for custom command project>",
        "region": "<Region for the speech service>",
        "keywordModelUrl": "https://aedspeechscenarios.blob.core.windows.net/keyword-tables/computer.table",
        "keyword": "computer"
    }
```

All settings can be found in Speech Studio -> Custom Commands -> target project -> Settings.
The keyword used below is a default publicly available keyword. If you wish to use your own, you can add your own custom keyword by uploading a created table file to blob storage. Blob storage needs to be configured with either anonymous container access or anonymous blob access. 

11. Click **Update**.
1. Click on the **Routes** tab at the top. Ensure you have a route with the following value:

```   
   FROM /messages/modules/azureearspeechclientmodule/outputs/* INTO $upstream
```   

13. Click **Review + Create**.
1. Click **Create**.
