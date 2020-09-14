# Connect to your Project Santa Cruz devkit through SSH or serial

Follow the steps below to setup an SSH or serial connection to your Project Santa Cruz Development Kit through [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

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

## Serial connection to the devkit

1. Connect your devkit to a serial port.

1. Power on your devkit.

1. In Windows, open Device Manager. Go to **Ports** and click **USB to UART** to open **Properties**. Note which COM port your device is connected to.

1. Click the **Port Settings** tab. Make sure **Bits per second** is set to 115200.

1. Open PuTTY. Enter the following and click **Open** to connect to your devkit via serial:

    1. Serial line: COM\<your COM port #>
    1. Speed: 115200
    1. Connection Type: Serial

    ![putty_serial](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/article_images/troubleshooting_putty.png)