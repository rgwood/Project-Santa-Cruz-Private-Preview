# Azure Edge Devices Overview

Azure Edge Devices (AED) provides advanced, end-to-end tools that enable you to rapidly prototype and develop smart devices at the edge of the cloud. With AED, you can choose off-the-shelf hardware to quickly develop and build proof-of-concept (POC) prototypes. AED even makes it possible to create your solutions with no coding.

After you develop your POC prototype, AED provides you with powerful tools to move into deployment and to manage your deployed edge AI solution. The AED tools enable you to securely integrate edge AI devices into into cloud-based services, update the devices when needed, and manage them at enterprise scales.

## What is the Edge?

Until recently, solutions and services that involve AI have typically hosted their AI's in data centers, which are also referred to as *clouds*. However, we are in the middle of a technology paradigm shift. Increasingly, businesses are connecting devices to the cloud's *edge*. Devices that exist at the cloud's edge process data close to the source where they obtain it. For example, a smart assistant program such as Cortana runs on a computer or mobile device that is close to or carried by the user. It connects to the cloud and shares specific data with the cloud for further processing.

## AI at the Edge

With the advent of the AI at the cloud's edge, you can put computing power locally, where it matters most, and offer instantaneous reactions to actionable data. The recent explosion of smart devices, Internet of Things (IoT) sensors, and intelligent edge devices offer a vastly increased level of computing power. They now support machine learning at the cloud's edge with the use of more efficient AI algorithms to offer instantaneous localized actionable data for better performance and security.

Flowing across and through this ecosystem of smart, cloud-connect edge devices is a constant stream of data you can capture and apply intelligence to to enable better decisions and transformative processes. It allows you to discover ways to do things differently, create new experiences, find new ways of working, and create new optimized outcomes. These new outputs in turn create new data which helps you learn more, refine things further, and bring more value to your company.

When creating an AI solution at enterprise scale, it is not an either-or, cloud vs. edge question. Instead, it is a question of cost, performance, and management optimization. There is likely to be an optimized mixture of cloud computing, scale, and management with edge performance and efficiency.

While cloud-based AI solutions have superior computational resources to manage massive amounts of data, they have their limitations as well. Cloud-based AI limitations include:
- **Latency**: An autonomous vehicle cannot wait even for a tenth of a second to activate emergency braking when the AI algorithm predicts an imminent collision.
- **Reliability**: Connectivity issues can be disastrous for mission critical applications such as fire detection.
- **Privacy**: Personal and corporate privacy becomes a concern when all data must traverse the internet.
- **Efficiency**: Continually streaming real-time HD video to the cloud for AI processing can be extremely expensive compared to local processing.

While intelligent edge devices have improved immensely with greater compute and better hardware, they have limitations as well. Intelligent edge device limitations include:
- **Limited computational power**: Unlike the cloud, there is only so much computational power you can put into a device such as a sensor or a camera.
- **Power source**: Edge devices are not always connected to a power source which raises the issue of battery life.
- **Management**: How do you manage a varied array of devices to ensure that they are working and that the firmware is up to date? How do you collect data centrally to see collective results?
- **Edge solution development**: How do you create a device-compatible solution and extend it to the rest of your AI solution?

As you can see from the limitations listed above, there is a place for both cloud and edge intelligence. However, this raises a larger question of overarching enterprise solution management. An optimal AI solution requires a robust AI platform that supports both cloud and edge AI design and management. In fact, Microsoft has found several common obstacles that are keeping our customers from reaching the edge as illustrated in the graphic below.
![Top Issues for Microsoft Customers that Inhibit Edge AI](getting_started/getting_started_images/aed-customer-top-issues.png)

As the figure above shows, there's a steep learning curve when it comes to migrating AI to the edge. It's hard to do matchmaking aross devices, skills, and solutions. Security of information is an impediment, as is monitoring devices and maintaining them. Migrating products and services that are currently not connected to the cloud is a problem for many solution implementers. Also, it's hard to find devices that are compatible with your solution and integrate them into your infrastructure.

## Microsoft and Edge AI
Microsoft's Azure Edge Devices offers Project Santa Cruz. Santa Cruz consists of the AED DevKit, as well as Azure-based resources that enable you to design, develop, deploy, and maintain edge AI solutions. It is designed to simplify planning, POC development, scaling to the enterprise level, deploying, integrating, and manageing complex AI solutions. It also offers opportunities to lower the cost of manufacturing and to reduce the complexity of provisioning. In addition, AED provides a secure management platform that operates at enterprise scale. 

Project Santa Cruz offers an end-to-end turnkey device lifecycle management solution by integrating the core device management services that Azure IoT provides. The core device management services include, but not limited to, IoT Hub, Device Provisioning Service (DPS), and IoT Edge. It also provides new OS and firmware update services and Azure Device Update. This means that Santa Cruz is Enterprise deployment and operation ready through the Azure portal. Santa Cruz utilizes each Azure IoT service’s unique capability to create a strong turnkey device management solution. For Santa Cruz, this starts from the manufacturing phase when hardware ventors build Azure-ready devices that can offer simple Azure provisioning steps for scalable deployment. These devices also provide seamless support of latest software payloads in Azure portal. Hardware partners can utilize Microsoft's end-to-end platform and plug in their solutions to this model through public APIs. 

![Comparing currently available edge AI options](getting_started/getting_started_images/aed-comparing-options.png)

The preceding figure shows that only Project Santa Cruz comes with the ability to develop no-code or low-code solutions. These incloude sample AI models that you can train to your individual needs, sample templates, and simple custom AI models that are targeted towars specific vertical markets. In addition, Project Santa Cruz provides you with the tools to design, prototype, and develop edge AI solutions from scratch. With Santa Cruz, you can build POC apps, and then securely move them into production and scale them to the enterprise level. 

## Next Steps
Now that you know what edge AI is, [find out what Microsoft Azure Edge Devices can do for you.](aed-intro.md)
