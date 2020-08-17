# Create a No Code Vision Solution and Deploy it to a Project Santa Cruz Dev Kit

Project Santa Cruz enables you to build a complete computer vision solution and deploy it to your Project Santa Cruz Dev Kit. This article will guide you through the process of training a vision AI model and deploying it to the dev kit.


## Prerequisites

* Project Santa Cruz Development Kit with the Azure Eye SoM connected.
* [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) complete.
* [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) complete.
* Default vision and web stream AI modules deployed.
* Azure subscription with the following services enabled:
    - Storage
    - Web
    - Cognitive Services

## Open Azure Edge Devices in the Azure Portal

The first step in creating a new vision solution is to select the Azure Edge device or devices to use.

1. Start your browser and sign into your [Azure account](https://preview.portal.azure.com/#home).

1. Use the **Search** box at the top of the page, enter **Azure Edge Devices**.

1. In the list that appears, choose, **Azure Edge Devices**. Your browser displays the Azure Edge Devices Overview.

Alternatively, you can go directly to the [Azure Edge Devices Overview](https://preview.portal.azure.com/#blade/AzureEdgeDevices/AEDBlade/overview) page.

## Create a vision prototype

1. On the **Azure Edge Devices Overview** page, click the **Demos & tutorials** tab.

    ![overview](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_overview.png)

1. Under **Vision tutorials and demos**, click **Create a vision prototype**.

    ![tutorials_and_demos](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_tutorials_and_demos.png)

1. On the **New AED Custom Vision prototype** page, do the following:

    1. In the **Project name** box, enter a name for your vision prototype.

    1. Enter a description of the vision prototype in the **Project description** box.

    1. Select **Santa Cruz Devkit** under the **Device type** drop-down menu.

    1. Select a resource under the **Resource** drop-down menu or create a new resource.

    1. In the **Project type** list, choose whether your vision project will perform object detection or image classification. For this Quickstart Guide, select **Object detection**.

    1. In the **Optimization** list, select whether you want to optimize your project for accuracy, low network latency, or a balance of both.

    1. Click the **I agree to terms & conditions for this project** checkbox. If you need to review the terms and conditions, select **See details**.

    1. Click the **Create** button.

    ![create_prototype](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_create_prototype.png)

The page that appears walks you through the remaining workflow that is required to get your project up and running.

## Connect a device to your project

After creating a Vision solution, you must add an IoT hub and at least one device to it.

1. In the **IoT Hub** pull-down list, select the IoT hub to which your devkit was provisioned during the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md).

1. In the **Devices** pull-down list, select your devkit.

![connect_device](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_connect_device.png)

## Capture images

Next, you need to either load images to train your AI model, or you must capture images from the Eye SoM. For this Quickstart Guide, we'll capture images.

1. Choose the **Capture Images** link under **Capture images from your device to use as training data**. Alternatively, you can choose **+Capture Images** from the menu near the top of the page.
2. In the pane that appears on the right side of the window, select **View device stream**. A tab appears in your browser that shows the device's input video stream.
3. Ensure that your Eye SOM camera is correctly aligned to take the training pictures. If the camera isn't aligned properly, make adjustments until you are satisfied.
4. Close the new browser tab and switch back to the tab containing your AED session.
5. Select the **Take Photo** button.

![capture_images](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_capture_images.png)

At this point, you can continue to take photos if you need more. For example, if your project monitors a store shelf stocked with products and sends a notification when the shelf needs restocking, you'll need a photo of the empty shelf, one of a fully stocked shelf, and several pictures of the shelf stocked to varying degrees.

When you have enough photos, choose the **Close** button.

## Label the images

For the AI to process the photos, you must label them with tags.

1. From **Label images and train model iteration**, select **Open project in Custom Vision**. Custom Vision pops up in a new browser tab.

    ![label_and_train](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_label_and_train.png)

1. Select the one or more of the images that you captured.

1. Near the top of the new browser tab, click the **Tag images** option.

1. In the **Image Tagging** dialog box that appears, enter a label for the image or images. For example, if you were creating an AI that would notify you when a store shelf needs restocking, you would select a photo of an empty shelf and then add the tag "Empty Shelf" to it. You might also add a tag that says "Full Shelf" to a photo of the fully-stocked shelf.

1. After adding a tag to an image, choose **Save and Close**.

## Train your model

After your images are labeled, you must train your AI model. To do so, click the **Train** button near the top of the browser tab. This may take a while if your image set is extremely large.

When the training has completed, you'll see the results. If you are satisfied, close Custom Vision by closing the browser tab. Select the **Azure Developer Portal** browser tab to continue.

## Deploy Your AI Model

Near the bottom of the **Azure Developer Portal** browser tab, you'll find the **Deploy Model** option. Click that to deploy your model.

![deploy_model](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_deploy_model.png)

## Next Steps

In this Quickstart Guide, you created a Vision project for your Eye SOM. You took pictures and used that input data to train your AI model. Finally, you deployed it to your Eye SOM. Next, try the [Quickstart Guide for the Ear SOM to create a speech solution](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/nocode-speech.md).



