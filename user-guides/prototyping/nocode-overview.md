# The No-Code Journey

Project Santa Cruz enables you to develop common types of AIs without needing to write programming code.

## Secure Hardware

The Santa Cruz development kit (DevKit) comes with hardware for creating vision and speech solutions. This hardware is built secure, meaning that
it can uniquely identify itself to the Azure cloud portal so that your solution can authorize the hardware to connect.

As a result, you don't have to design, build, and program unique hardware that you probably won't be able to reuse in other applications.
By having off-the-shelf hardware that you can build your applications on, you can create a variety of edge AI applications without writing any
source code.

## Pre-Trained AI Models

The Azure Edge Devices (AED) portal enables you to build solutions with no code and deploy them to your hardware. You can use the pre-trained AI
models that the portal provides. Pre-trained models are targeted towards specific vertical markets, so they "know" how to handle the input data
your devices send them. With pre-trained models, you can not only build solutions with no coding, you can avoid having to gather the large
volumes of data necessary for training.

An example of a pre-trained model that's in the AED portal is the hospitality model. It's designed to enable you to build a voice
assistant that you can use to control electrical devices in a hotel room with your voice.

## Untrained AI Models

You can also use AI models that are provided by the portal but not trained. Like pre-trained models, untrained models let you build
solutions without having to write source code. An example of a trainable model provided by the portal is the object detection model. When you use
it, you can train it by uploading pictures to it or by taking pictures with the Eye SOM that comes in the DevKit. The object detection model
then examines the differences between the pictures to find what it needs to watch for.

## Portal-Based Deployment

The AED portal provides you with the ability to easily provision your AI model on your hardware. It's just a matter of selecting some menu
choices and inputting some basic information. You don't need to learn tedious hardware-specific deployment methods such as JTAG. And with the
portal, you can provision many devices quickly, rather than manually deploying to each individual device one by one.

## Monitor Performance

Because Project Santa Cruz is integrated with Azure, you can use Azure tools and services in your solution. For example, you could download
Azure IoT Explorer and use it to monitor your AI model's performance. The information you receive can then help you improve your AI model.

## Production, Management, and Scaling

You can use the AED portal to move to your proof-of-concept solution into production, manage your solution, and scale to any size. The portal
can handle one device or thousands.

## Next Steps

The following Getting Started Guides help you get up and running quickly with producing no-code solutions and proof-of-concept demos.

[Quickstart: Create a Vision Solution using the DevKit](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/aed-create-nocode-vision.md)

[Quickstart: Create a Voice Assistant with the Devkit](https://github.com/Azure/AI-at-Edge-Preview/blob/main/user_guides/aed-nocode-speech.md)
