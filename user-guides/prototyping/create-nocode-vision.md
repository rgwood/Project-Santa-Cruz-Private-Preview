# Create a no-code vision solution and deploy it to a Project Santa Cruz Development Kit

Project Santa Cruz enables you to build and deploy complete computer vision solutions, from simple no-code models to more advanced solutions. This article will guide you through the process of creating, training, and deploying a custom object detection or image classification model to your devkit. This is a no-code solution that is suitable for developers with little to no AI experience and those just getting started with Project Santa Cruz.

## Prerequisites

* Project Santa Cruz Development Kit with the Azure Eye SoM connected.

* [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) complete.

* [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) complete.

## Project Santa Cruz in the Azure Portal

1. Open a browser and sign into your [Azure account](https://preview.portal.azure.com/#home).

1. In the **Search** box at the top of the page, enter **Project Santa Cruz**.

1. Select **Project Santa Cruz** under **Services**.

Alternatively, you can navigate directly to the [Project Santa Cruz Overview page](https://go.microsoft.com/fwlink/?linkid=2135819).

## Create a vision prototype

1. On the **Project Santa Cruz Overview** page, click the **Demos & tutorials** tab.

    ![overview](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_overview.png)

1. Under **Vision tutorials and demos**, click **Create a vision prototype**.

    ![tutorials_and_demos](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_tutorials_and_demos.png)

1. On the **New Santa Cruz Custom Vision prototype** page, do the following:

    1. In the **Project name** box, enter a name for your vision prototype.

    1. Enter a description of the vision prototype in the **Project description** box.

    1. Select **Santa Cruz Devkit** under the **Device type** drop-down menu.

    1. Select a resource under the **Resource** drop-down menu or create a new resource.

    1. In the **Project type** list, choose whether your vision project will perform object detection or image classification. For more information on the project types, click **Help me choose**.

    1. In the **Optimization** list, select whether you want to optimize your project for accuracy, low network latency, or a balance of both.

    1. Click the **Create** button.

    ![create_prototype](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_create_prototype.png)

## Connect a device to your project

After creating a vision solution, you must add a device and its corresponding IoT Hub to it.

1. Power on your devkit.

1. In the **IoT Hub** pull-down list, select the IoT hub to which your devkit was provisioned during the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md).

1. In the **Devices** pull-down list, select your devkit.

![connect_device](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_connect_device.png)

## Capture images

Next, you must either load images or capture images for training your AI model. We recommended uploading at least 30 images per tag type. For example, if you want to build a dog and cat detector, you must upload at least 30 images of dogs and 30 images of cats. To capture images with the Eye SoM of your devkit, do the following:

1. On your vision project page, click **Capture images** under **Capture images from your device to use as training data**. Alternatively, you can choose **+ Capture images** from the menu near the top of the page.

1. In the **Image capture** window, select **View device stream** to view the Eye SoM video stream.

1. Check the video stream to ensure that your Eye SoM camera is correctly aligned to take the training pictures. Make adjustments as necessary.

1. In the **Image capture** window, click **Take photo**.

    ![capture_images](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_capture_images.png)

1. Alternatively, set up an automated image capture to collect a large quantity of images at a time by checking the **Automatic image capture** box. Select your preferred imaging rate under **Capture rate** and the total number of images you would like to collect under **Target**. Click **Set automatic capture** to begin the automatic image capture process.

    ![automatic_image_capture](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_automatic_image_capture.png)

When you have enough photos, click **Close**. All images will be saved in [Custom Vision](https://www.customvision.ai/).

## Label the images

Before training your model, add labels to your images.

1. Under **Label images and train a model iteration**, select **Open project in Custom Vision**.

    ![label_and_train](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_label_and_train.png)

1. On the **Custom Vision** page, select one or more of your unlabeled images.

1. Near the top of the page, click **Tag images**.

1. In the **Image Tagging** dialog box, enter a label for each selected image. For example, if you were creating a vision solution that would notify you when a store shelf needs restocking, add the tag "Empty Shelf" to images of empty shelves, and add the tag "Full Shelf" to images of fully-stocked shelves. If you selected object detection as your project type, make sure to draw [bounding boxes](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/get-started-build-detector#upload-and-tag-images) around each labeled object in your images.

1. After labeling your images, click **Save and Close**.

## Train your model

After your images are labeled, you are ready to train your AI model. To do so, click **Train** near the top of the page. Training typically takes about 30 minutes, but may take longer if your image set is extremely large.

When the training has completed, you'll be able to [evaluate the results](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/get-started-build-detector#evaluate-the-detector). After training, [test your model](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/test-your-model) on additional images and retrain as necessary. Each time you train your model, it will be saved as a new iteration. Reference the [Custom Vision documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-improving-your-classifier) for additional information on how to improve model performance.

Once you are satisfied with the performance of your model, close Custom Vision by closing the browser tab.

## Deploy Your AI Model

On your vision project page in the Project Santa Cruz portal, click **Deploy Model** to deploy your model to your devkit.

![deploy_model](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/no_code_vision_deploy_model.png)

After deploying your model, [view your device's video stream](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision_view_video-stream.md) to see your model inferencing in action.

## Provide feedback

After completing the no-code vision solution, please provide feedback on your experience via this [questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRzoJxrXKT0dEvfQyxsA0h8lUMTc0N1U3SUhFTlZZMEdZVU45NVpNQkZFWC4u). Your feedback will help us continue to fine-tune and improve the no-code vision experience.

For more information on Project Santa Cruz Quests and to provide feedback on other experiences, please visit the [test scenarios page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/test-scenarios.md).

## Next Steps

In this quickstart guide, you created a no-code vision solution for your Project Santa Cruz Development Kit. You collected and labeled images, which were used to train your AI model. Finally, you deployed the model to your devkit. Next, create a [no-code speech solution](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/nocode-speech.md).
