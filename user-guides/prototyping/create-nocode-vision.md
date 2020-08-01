# Quickstart: Create a Vision Solution using the AED DevKit

In this quickstart, you start a new Vision solution with the Azure Edge Devices Development Kit (AED DevKit) to integrate AI into Edge devices.

If you do not have an [Azure subscription](https://docs.microsoft.com/en-us/azure/guides/developer/azure-developer-guide#understanding-accounts-subscriptions-and-billing), please create a [free account](https://azure.microsoft.com/free/?ref=microsoft.com&utm_source=microsoft.com&utm_medium=docs&utm_campaign=visualstudio) before you begin.

## Prerequisites

* Installed AED DevKit.
* Eye SOM whose carrier board is connected to an IoT Hub.
* Default vision and web stream AI modules deployed.
* Azure tennant ID enrolled in the AED private preview with the following registered resources.
 - Storage
 - Web
 - Cognitive Services

## Select the Azure Edge Devices in the Azure Portal

The first step in creating a new solution is to select the Azure Edge device or devices to use.

1. Start your browser and sign into your [Azure account](https://preview.portal.azure.com/#home).
2. Use the **Search** box at the top of the page, enter **Azure Edge Devices**.
3. In the list that appears, choose, **Azure Edge Devices**. Your browser displays the Azure Edge Devices Overview.

Alternatively, you can go directly to the [Azure Edge Devices Overview](https://preview.portal.azure.com/#blade/AzureEdgeDevices/AEDBlade/overview) page.

## Make a New Vision Solution

1. On the **Azure Edge Devices Overview** site, choose the **Demos & Tutorials** tab.
2. Under **Vision tutorials and demos**, choose the **Create a vision prototype** option. Your browser displays the **New AED Custom Vision prototype** page.
3. In the uppermost text box, type the name of your vision project.
4. Enter the project description in the next text box.
5. From the **Resource** pull-down box, choose any resources you may need for your project. The Azure resources you use must be part of your subscription.
6. In the **Project type** list, choose whether your Vision project will perform object detection or image classification using. For this Quickstart Guide, select **Object detection**.
7. In the **Optimization** list, select whether you want to optimize your project for accuracy, low network latency, or a balance of both.
8. Click the **I agree to terms & conditions for this project** checkbox. If you need to review the terms and conditions, select **See details**.
9. Click the **Create** button.

The page that appears walks you through the remaining workflow that is required to get your project up and running.

## Connect a Device to Your Project

After making a Vision solution, you must add an IoT hub and at least one device to it.

1. In the **IoT Hub** pull-down list, select the IoT hub that you'll be using for this project.
2. In the **Devices** pull-down list, choose the Eye SOM that is attached to the IoT hub.

## Capture Images
Next, you need to either load images to train your AI model, or you must capture images from the Eye SOM. For this Quickstart Guide, we'll capture images.

1. Choose the **Capture Images** link under **Capture images from your device to use as training data**. Alternatively, you can choose **+Capture Images** from the menu near the top of the page.
2. In the pane that appears on the right side of the window, select **View device stream**. A tab appears in your browser that shows the device's input video stream.
3. Ensure that your Eye SOM camera is correctly aligned to take the training pictures. If the camera isn't aligned properly, make adjustments until you are satisfied.
4. Close the new browser tab and switch back to the tab containing your AED session.
5. Select the **Take Photo** button. 

At this point, you can continue to take photos if you need more. For example, if your project monitors a store shelf stocked with products and sends a notification when the shelf needs restocking, you'll need a photo of the empty shelf, one of a fully stocked shelf, and several pictures of the shelf stocked to varying degrees.

When you have enough photos, choose the **Close** button.

## Label the Images

For the AI to process the photos, you must label them with tags.

1. From **Label images and train model iteration**, select **Open project in Custom Vision**. Custom Vision pops up in a new browser tab.
2. Select the one or more of the images that you captured.
3. Near the top of the new browser tab, you'll see the **Tag images** option. Choose it.
4. In the **Image Tagging** dialog box that appears, enter a label for the image or images. For example, if you were creating an AI that would notify you when a store shelf needs restocking, you would select a photo of an empty shelf and then add the tag "Empty Shelf" to it. You might also add a tag that says "Full Shelf" to a photo of the fully-stocked shelf. 
5. After adding a tag to an image, choose **Save and Close**.

## Train Your Model

After your images are labeled, you must train your AI model. To do so, click the **Train** button near the top of the browser tab. This make take a while of your image set is extremely large. 

When the training has completed, you'll see the results. If you are satisfied, close Custom Vision by closing the browser tab. Select the **Azure Developer Portal** browser tab to continue.

## Deploy Your AI Model

Near the bottom of the **Azure Developer Portal** browser tab, you'll find the **Deploy Model** option. Click that to deploy your model.

## Next Steps

In this Quickstart Guide, you created a Vision project for your Eye SOM. You took pictures and used that input data to train your AI model. Finally, you deployed it to your Eye SOM. Next, try the [Quickstart Guide for the Ear SOM to create a speech solution](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/nocode-speech.md).



