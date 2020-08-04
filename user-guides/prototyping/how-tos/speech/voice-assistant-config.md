# Managing your voice assistant

This article describes configuration of the voice assiztant application. 
For a step-by-step tutorial that guides you through the process of creating a voice assistant, see [QuickStart: Creating a Voice Assistant with the Project Santa Cruz Devkit](../nocode-speech.md).

## Keyword

A keyword is a word or short phrase which allows your product to be voice activated. For example, "Hey Cortana" is the keyword for the Cortana assistant. Voice activation allows your users to start interacting with your product completely hands-free by simply speaking the keyword. As your product continuously listens for the keyword, all audio is processed locally on the user's device until a detection occurs to ensure their data stays as private as possible. 

### Configure keyword in the demo window

1. Click on *change* link near custom keyword.
2. Select one of the available keywords. 
3. Click **Save** to apply changes.
4. Led lights on the Ear SOM will change to the 3 bright blue when configuration is completed.

### Configure keyword in the device configuration

1. Click on **Devices** in the left navigation menu.
2. Find your device in the list and click on it - device window will open.
3. Open **Speech** tab.
4. Click on *change* link near custom keyword.
5. Select one of the available keywords. 
6. Click **Save** to apply changes.
4. Led lights on the Ear SOM will change to the 3 bright blue when configuration is completed.

## Create custom keyword

You can create a unique name for your voice assistant. It takes up to 30 minutes to train basic custom keyword model.

### Using Speech Studio

Use Speech Studio to create a custom keyword. <br>
Follow these [instructions](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-devices-sdk-create-kws) to create custom keyword. <br>
Once configured, the keyword will be available for conifuration in the portal.

## Configure commands

Custom Commands makes it easy to build rich voice commanding apps optimized for voice-first interaction experiences. Custom Commands is best suited for task completion or command-and-control scenarios.

### Using speech demo window

1. Click on *change* link near custom commands.
2. Select one of the available custom commands.
3. Click **Save** to apply changes. 

### Using device configuration window

1. Click on **Devices** in the left navigation menu.
2. Find your device in the list and click on it - device window will open.
3. Open **Speech** tab.
4. Click on *change* link near custom commands.
5. Select one of the available custom commands.
6. Click **Save** to apply changes 

## Create custom commands

You can manage commands for your voice assistant application to execute.

### Using Speech Studio

Use Speech Studio to create custom commands. <br>
Follow these [instructions](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-custom-commands-application).<br>
Once configured, the custom commands will be available for conifuration in the portal.
