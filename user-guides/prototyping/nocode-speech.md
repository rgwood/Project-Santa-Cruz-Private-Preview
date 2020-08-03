# Quickstart: Creating a Voice Assistant with the AED Devkit

In this quickstart, you make your own voice assistant using the Project Santa Cruz Development Kit (DevKit) and [Speech services](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview).

## Prerequisites

* Hardware: 
  * Devkit with Ear SOM connected.
  * Speaker connected to the Ear SOM (not included in the package).
* Configuration steps: 
  * [OOBE (out of box experience)](../getting_started/oobe.md) setup completed.
* Organization Azure tenant id enrolled in the Project Santa Cruz private preview.
* The following resource provides registered in the Azure subscription:
  * Cognitive Services
  * Storage
  * Web 

## Go to Azure Edge Devices in the Azure portal

The first step in creating a voice assistant is to navigate to the Project Santa Cruz in Azure portal.

1. Start your browser and go to the [Azure preview portal](https://preview.portal.azure.com/#home).
2. Sign into your Azure account. 
2.	Use the Search box at the top of the page, enter *Azure Edge Devices*.
3.	In the list that appears, choose *Azure Edge Devices*. Your browser displays the Azure Edge Devices Overview page.

Alternatively, you can navigate directly to the [Azure Edge Devices Overview page](https://preview.portal.azure.com/#blade/AzureEdgeDevices/AEDBlade/overview).


![Azure Edge Devices Portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/aed-portal-home-page.png)


## Create voice assistant using templates

You can build a voice assistant using available templates. The Hospitality template is available for the private preview. Healthcare is also scheduled to be released soon.

1.	Open **Demos & Tutorials** tab. 
2.	Click **Try out speech themes** under **Speech tutorials and demos**.
3.	Select IoT hub to which your device is connected from the **IoT hub** list.
4. Choose the device from the list.
5.	Select one of the speech templates.
6. Click the **I agree to terms & conditions for this project.** checkbox.
7.	Click **Create** button. The portal deploys the resource to the device.


![Azure Edge Devices Portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/aed-try-speech-themes.png)

8. Select the Azure subscription you're using for this project in the **Subscription** box.
9. Select the resource group to use from the **Resource group** list.
10. Enter name for the voice assistant. It will be used as a prefix to resource names.
11. Select the region to deploy resources to from the **Region** list.
12. Choose the pricing tier from the **Tier** list. (We recommend **Standard**).
13. Click the **Create** button. Resources for the voice assistant application will be deployed to your subscription. <br/>
   
**WARNING:** Do not close the pane until the portal finish deploying the resource. Closing the pane can result in unexpected behavior from the device.
   
At this point, the portal displays the speech demo.

## Configure a keyword for your device

Next, you can add a keyword to your device so that you can activate it using voice. You can use prebuilt keywords and custom keywords created in [Speech Studio](https://speech.microsoft.com/).

1. Click on **change** link near **Custom keyword**.
2.	Select one of the available keywords. 

## Test out your voice assistant

Try any of the following commands to interact with your voice assistant. Always start with the keyword that you configured. For example - *Computer, turn on TV*.
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
