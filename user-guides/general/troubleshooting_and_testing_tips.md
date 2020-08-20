# Troubleshooting and testing tips for the Project Santa Cruz Development Kit

## SSH into the devkit

1. Install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

1. Plug in the carrier board power cable and turn on the device.

1. If a Wi-Fi connection has not yet been set up through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md), connect to the devkit's Wi-Fi AP:

    1. SSID: scz-xxxx (where xxxx = the last four digits of the devkit's WiFi MAC address)
    1. password = santacruz

    ![wifi_ap](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_wifi_ap.png)  

1. Open PuTTY. Enter the following and click **Open** to SSH into your devkit:

    1. Host Name: 10.1.1.1
    1. Port: 22
    1. Connection Type: SSH

    ![putty](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_putty.png)  

1. Log in to the PuTTY terminal. If you set up an SSH username and password during the [OOBE]( https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md), enter those login credentials when prompted. Otherwise, enter the following:  

    1. login as: root
    1. Password: p@ssw0rd

    ![putty_login](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/usb_putty_login.png)  


## Docker troubleshooting commands

|Command:                        |Function:                  |
|--------------------------------|---------------------------|
|docker ps                       |shows which containers are running |
|docker images                   |shows which images are on the device |
|docker rmi \<image id> -f       |deletes an image from the device |
|docker logs -f edgeAgent <br> docker logs -f \<module_name> |takes container logs of specified module |


## Ear SoM and speech module troubleshooting

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

## Other device commands

To run these commands, connect to the devkit's Wi-Fi AP (if a Wi-Fi connection has not yet been set up through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md)), SSH into the devkit using PuTTY, and enter the commands in the PuTTY terminal.

|Category:         |Command:                    |Function:                  |
|------------------|----------------------------|---------------------------|
|OS                |cat /etc/os-release         |check Mariner image version |
|OS                |cat /etc/os-subrelease      |check derivative image version |
|OS                |cat /etc/adu-version        |check ADU version |
|Temperature       |cat /sys/class/thermal/thermal_zone0/temp |check temperature of devkit |
|Wi-Fi             |journalctl -u hostapd.service |check SoftAP logs|
|Wi-Fi             |journalctl -u wpa_supplicant.service |check Wi-Fi services logs |
|Wi-Fi             |journalctl -u ztpd.service  |check Wi-Fi Zero Touch Provisioning Service logs |
|Wi-Fi             |journalctl -u systemd-networkd |check Mariner Network stack logs |
|OOBE              |journalctl -u oobe -b       |check OOBE logs |

Note: The Wi-Fi commands can be combined into the following:

```console
journalctl -u hostapd.service -u wpa_supplicant.service -u ztpd.service -u systemd-networkd -b 
```

## USB Updating 

|Error:                                    |Solution:                                               |
|------------------------------------------|--------------------------------------------------------|
|LIBUSB_ERROR_XXX during USB flash via UUU |This error is the result of a USB connection failure during UUU updating. If the USB cable is not properly connected to the USB ports on the PC or the PE-10X, an error of this form will occur. Try unplugging and replugging both ends of the USB cable and jiggling the cable to ensure a secure connection. This almost always solves the issue. |