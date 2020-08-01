# Quickstart: Creating a Voice Assistant with the AED Devkit

In this quickstart, you make your own voice assistant with the Azure Edge Devices Development Kit (AED DevKit).

## Prerequisites

* Hardware: Devkit with Ear SOM.
* Configuration steps: 
  * OOBE setup completed.
  * Devkit connected to an IoT Hub.
  * Sample speech module deployed: “azureearspeechclientmodule”
* Azure tenant id enrolled in AED private preview.
* The following resource provides registered in the Azure subscription:
  * Storage
  * Web
  * Cognitive Services

## Go to Azure Edge Devices in the Azure portal

The first step in creating a voice assistant is to navigate to the Azure Edge Devices portal.

1. Start your browser and go to the [Azure preview portal](https://preview.portal.azure.com/#home).
2. Sign into your Azure account. 
2.	Use the Search box at the top of the page, enter Azure Edge Devices.
3.	In the list that appears, choose, Azure Edge Devices. Your browser displays the Azure Edge Devices Overview page.

Alternatively, you can navigate directly to the [Azure Edge Devices Overview page](https://preview.portal.azure.com/#blade/AzureEdgeDevices/AEDBlade/overview).

![Azure Edige Devices Portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/aed-portal-home-page.png)


## Select a Speech Template

You can build a voice assistant using available templates. The Hospitality theme is available for the private preview. Healthcare is also scheduled to be released soon.

1.	Open **Demos & Tutorials** tab. 
2.	Click **Try out speech themes** under **Speech tutorials and demos**.
3.	Select an IoT hub instance from the **IoT hub** list.
1. Choose your device from the list.
4.	Select one of the speech templates.
1. Click the **I agree to terms & conditions for this project.** checkbox.
5.	Click **Create** button. The portal deploys the resource to the device.
   ![Azure Edige Devices Portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/aed-try-speech-themes.png)

**WARNING:** Do not close the **Try out speech themes** pane until the portal finish deploying the resource. Closing the pane can result in unexpected behavior from the device.
   
6. Select the Azure subscription you're using for this project in the **Subscription** box.
7. Select the resource group to use from the **Resource group** list.
8. Enter name for the voice assiatnt. It will be used as a prefix to resource names..
9. Select the region for your project's deployment from the **Region** list.
10. Choose the pricing tier from the **Tier** list. (We recommend **Standard**).
11. Click the **Create** button. Resources for the voice assistant application will be deployed to your subscription. <br/>
   
**WARNING:** Do not close the pane until the portal finish deploying the resource. Closing the pane can result in unexpected behavior from the device.
   
At this point, the portal displays the speech demo.

## Configure a Keyword for Your Device

Next, you can add a keyword to your device so that you can activate it using voice. You can use prebuilt keywords and custom keywords created in Speech Studio.

1. Click on **change** link near **Custom keyword**.
2.	Select one of the available keywords. 

## Test Out Your Voice Assistant

Try any of the following commands to interact with your voice assistant. Always start with the keyword that you configured, for example, "Computer, turn on TV."
* "Turn on lights."
* "Turn off lights."
* "Turn on TV."
* "Turn off TV."
* "Turn on AC."
* "Turn off AC."
* "Open blinds."
* "Close blinds."
* "Set temp to 75."
   
## Next Steps

Now that you have created a voice assistant, you could try creating a [Vision project](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/create-nocode-vision.md).
