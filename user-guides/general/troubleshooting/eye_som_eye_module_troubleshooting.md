# Eye SoM and eye module troubleshooting

## Eye module troubleshooting tips

In case of problems with **WebStreamModule**, ensure that **azureeyemodule**, which does the vision model inferencing, is running. To check the runtime status, go to the [Azure portal](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) and navigate to **All resources** -> **\<your IoT hub>** -> **IoT Edge** -> **\<your device ID>**. Click the **Modules** tab to see the runtime status of all installed modules.

![runtime_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_iot_edge_device_page.png)

If the runtime status of **azureeyemodule** is not listed as **running**, click **Set modules** -> **azureeyemodule**. On the **Module Settings** page, set **Desired Status** to **running** and click **Update**.

 ![desired_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/firmware_desired_status_stopped.png)


## View device RTSP video stream

View your device's RTSP video stream through the [Project Santa Cruz portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision_view_video-stream.md) or [VLC media player](https://www.videolan.org/vlc/index.html).

To open the RTSP stream in VLC media player, go to **Media** -> **Open network stream** -> **rtsp://[device IP address]/result**.