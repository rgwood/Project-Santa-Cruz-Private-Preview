# Ear SoM and speech module troubleshooting

- Access speech module logs:
    - If a Wi-Fi connection has not yet been set up through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md), connect to the devkit's Wi-Fi AP.
    - SSH into the devkit with PuTTY.
    - In the PuTTY terminal, enter the following:
        ```console
         iotedge logs azureearspeechclientmodule
        ```

- If you cannot create a new or use an existing voice assistant, do the following:
    - Check if the runtime status of **azureearspeechclientmodule** is not listed as **running**. To locate the runtime status of your device modules, open the [Azure portal](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) and navigate to **All resources** -> **\<your IoT hub>** -> **IoT Edge** -> **\<your device ID>**. Click the **Modules** tab to see the runtime status of all installed modules.

    ![runtime_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_iot_edge_device_page.png)

    If the runtime status of **azureearspeechclientmodule** is not listed as **running**, click **Set modules** -> **azureearspeechclientmodule**. On the **Module Settings** page, set **Desired Status** to **running** and click **Update**.

    ![desired_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/firmware_desired_status_stopped.png)

    - Check if the Ear SoM LEDs are green. If the left LED is green, this indicates that the device is powered on. If the center LED is also blinking green, this indicates that authentication is in progress. All three LEDs will change to blue once the device is authenticated and ready to use.

### Ear SoM LED indicators

|LED State:                  |Ear SoM Status:            |
|----------------------------|---------------------------|
|1x green (left LED)         |power on |
|1x green (left LED) <br> 1x blinking green (center LED) |authentication in progress |
|3x off                      |initialization completed |
|3x blue                     |ready for use |
|3x blinking blue            |keyword recognized |
|3x racing blue              |processing |
|3x red                      |mute |