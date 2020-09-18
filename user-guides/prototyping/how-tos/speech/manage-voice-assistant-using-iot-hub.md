# Managing your voice assistant using IoT Hub

This article describes how you can configure your voice assistant application using IoT Hub only.
For a step-by-step tutorial that guides you through the process of creating a voice assistant using demo template, see [QuickStart: Creating a Voice Assistant with the Project Santa Cruz Devkit](../../nocode-speech.md).

1. Open the [Azure portal](https://portal.azure.com) and locate your IoT Hub.
1. Select **IoT Edge** under **Automatic Device Management** in the left navigation menu.
1. Select the device that you wish to configure.
1. Click on **Set Modules**.
1. Verify that the following entry is present in the container registry credentials. Add credential is required.

Name|Address|Username|Password
----|-------|--------|--------
azureedgedevices|azureedgedevices.azurecr.io|devkitprivatepreviewpull|***

**NOTE:** If you do not have a password for the container registry, please reach to your primary contact for the Santa Cruz private preview program.

1. In the **IoT Edge Modules** section, select **azureearspeechclientmodule**.
1. Click on the **Module Settings** tab. Verify configuration.

Image URI|Restart Policy|Desired Status
---------|--------------|--------------
azureedgedevices.azurecr.io/azureearspeechclientmodule:preload-devkit |always|running

1. Click on the **Environment Variables** tab. Verify that there are no environment variables defined.
1. Click on the **Container Create Options** tab.

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

1. Click on the **Module Twin Settings** tab. Update the *speechConfigs* section as follows:

```
    "speechConfigs": {
        "appId": "<Application id for custom command project>",
        "key": "<Speech Resource key for custom command project>",
        "region": "<Region for the speech service>",
        "keywordModelUrl": "https://aedspeechscenarios.blob.core.windows.net/keyword-tables/computer.table",
        "keyword": "computer"
    }
```

Note: The keyword used above is a default publicly available keyword. If you wish to use your own, you can add your own custom keyword by uploading a created table file to blob storage. Blob storage needs to be configured with either anonymous container access or anonymous blob access.

To locate your **appID**, **key**, and **region**, go to [Speech Studio](https://speech.microsoft.com/):

- Sign in and select the appropriate speech resource.

- On the **Speech Studio** home page, click on **Custom Commands** under **Voice Assistants**.

    ![custom_commands](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/user-guides/prototyping/how-tos/speech/article_images/speech_custom_commands.png)

- Select your target project.

    ![project](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/user-guides/prototyping/how-tos/speech/article_images/speech_project.png)

- Click on **Settings** on the left-hand menu panel.

    ![project_settings](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/user-guides/prototyping/how-tos/speech/article_images/speech_project_settings.png)

- The **appID** and **key** will be located under the **General** settings tab.

    ![general_settings](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/user-guides/prototyping/how-tos/speech/article_images/speech_general_settings.png)

- To find your **region**, open the **LUIS resources** tab within the settings. The **Authoring resource** selection will contain region information.

    ![luis_resources](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/tree/main/user-guides/prototyping/how-tos/speech/article_images/speech_luis_resources.png)

1. Click **Update**.

1. Click on the **Routes** tab at the top. Ensure you have a route with the following value:

```
   FROM /messages/modules/azureearspeechclientmodule/outputs/* INTO $upstream
```

1. Click **Review + Create**.

1. Click **Create**.
