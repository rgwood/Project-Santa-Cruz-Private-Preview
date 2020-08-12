<!---
title: Azure eye SoM datasheet                     # the article title to show on the browser tab
description: Provides a list of important technical specifications for the Azure Eye SoM.              # 115 - 145 character description to show in search results
author: elqu20      # the author's GitHub ID - will be auto-populated if set in settings.json
ms.author: v-elqu     # the author's Microsoft alias (if applicable) - will be auto-populated if set in settings.json
ms.date: {@date}           # the date - will be auto-populated when template is first applied
ms.topic: reference  # the type of article
--->
# Project Santa Cruz eye SoM datasheet



|Product Specification           |     |
|--------------------------------|--------|
|Industrial Design               |Non-standalone Hardware Module       |
|Performance                     |2-4 TOPS, 0.5 W/TOPS   |
|Target Industries               |Manufacturing <br> Smart Buildings <br> Auto <br> Retail  |
|Hero Scenarios                  |Shopper Analytics <br> On-shelf Availability <br> Shrink Reduction <br> Security/Surveillance <br> Workplace Safety|
|Price                           |$50 MSRP  |
|Included in Box                 |1x AI Vision SoM |
|Dimensions                      |42mm x 42mm x 40mm   |
|Weight                          |TBD          |
|OS                              |NA           |
|Management Control Plane        |ADU          |
|Supported Software and Services |Azure IoT Hub <br> Azure IoT Edge <br> Azure Machine Learning <br> Azure Device Update <br> ONNX <br> OpenVINO        |
|General Processor               |NA         |
|AI Acceleration                 |Intel Movidius Myriad X (MA2085) VPU Vision Processing Unit (VPU) with Intel Camera ISP integrated       |
|Sensors and Visual Indicators   |Camera: Omni Vision 5670 <br> Lens: GSO GS8882AA (Resolution: 5MP at 30FPS, Distance: 50cm - infinity, FoV: 120 degrees, Color: Wide Dynamic Range, Fixed Focus Rolling Shutter)          |
|Camera Support                  |RGB, IR, and Depth cameras <br> 2 cameras can be run simultaneously|
|Integrated Graphics             |NA       |
|Security Crypto-Controller      |ST-Micro STM32L462CE      |
|Versioning / ID Component       |64kb EEPROM |
|Connectivity                    |NA      |
|Storage                         |NA     |
|Memory                          |LPDDR4 2GB     |
|Power                           |     |
|Ports                           |1x USB 3.0 Type C <br> 2 MIPI 4 Lane (up to 1.5 Gbps per lane)     |
|Control Interfaces              |x2 I2C <br> x2 SPI <br> x6 PWM (GPIOs, e.g. x2 clock, x2frame sync, x2 unused) <br> x2 spare GPIO |
|Protection                      |IP50    |
|Certification                   |CE <br> FCC     |
|Operating Temperature           |0 to 27 degrees C     |
|Touch Temperature               |<= 48 degrees C |
|Relative Humidity               |8% to 90%    |
|Noise                           |NA     |
|Shock                           |     |
|Vibration                       |2.0Grms from 1 to 300Hz.     |
|Drop Requirement                |     |