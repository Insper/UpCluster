# UpBoard Configuration

**Login ID: ubuntu** 

**PASSWORD:turin**

<aside>
⚠️ This instruction was tested on Upboard with Ubuntu 20.04

</aside>

## Sistem Operational Installation

1. Download Ubuntu 20.04.4 ISO from the Ubuntu download page, we used server edition

[](https://releases.ubuntu.com/20.04/ubuntu-20.04.5-live-server-amd64.iso)

2. Burn the downloaded image on a USB stick. We suggest using etcher or rufus for doing that. You can download the suggested software from:

[https://etcher.io](https://etcher.io/)

[https://rufus.ie](https://rufus.ie/)

3.  Insert the USB installer disk in an empty USB port and proceed with a normal Ubuntu installation.

## Setup UpBoard kernel

To access the upboard gpios, we need to change the default kernel to UpBoard kernel.

1. Add the upboard repository:

```bash
sudo apt update && sudo apt upgrade
```

```bash
sudo add-apt-repository ppa:up-division/5.4-upboard
```

2. Update the repository list

```bash
sudo apt update
```

3. Remove all the generic installed kernel

```bash
sudo apt autoremove --purge linux-*generic
```

4. Install the tested kernel:

```bash
sudo apt-get install linux-generic-hwe-18.04-5.4-upboard
```

5. Install the updates:

```bash
sudo apt dist-upgrade -y
sudo update-grub
```

6. Reboot the system

```bash
sudo reboot
```

7. Test if all is done right:

```bash
uname -a

Linux upxtreme-UP-WHL01 5.4.0-1-generic #2~upboard2-Ubuntu SMP Thu Jul 25 13:35:27 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```

## Configuring drivers

To be able to use the GPIO, PWM, SPI, I2C and UART functionality with a normal user

1. Install the upboard-extras

```bash
sudo apt install upboard-extras
```

2. Add the user that needs to access the HAT funcionality
    
    GPIO
    
    ```bash
    sudo usermod -a -G gpio $USER
    ```
    
    LEDs
    
    ```bash
    sudo usermod -a -G LEDS $USER
    ```
    
    SPI
    
    ```bash
    sudo usermod -a -G SPI $USER
    ```
    
    I2C
    
    ```bash
    sudo usermod -a -G i2c $USER
    ```
    
    UART
    
    ```bash
    sudo usermod -a -G dialout $USER
    ```
    

3. Reboot the system to apply the permission changes

```bash
sudo reboot
```

## Installing RPi.GPIO library

To have access to GPIO with python, install the RPi.GPIO lib for upboard

4. This package provides a class to control the GPIO on a Raspberry Pi, ported
to work on the UP board hardware, Download the GitHub

```bash
sudo apt install python3-pip
```

```bash
git clone https://github.com/emutex/RPi.GPIO.git
```

5. Install the package 

```bash
cd RPi.GPIO 
sudo python3 setup.py install

```

6. Clone Blinkt repository

```bash
cd 
git clone https://github.com/pimoroni/blinkt.git
```

7. Install the blinkt package 

```bash
sudo pip install blinkt
```

8. Run one example

```bash
python3 /home/ubuntu/blinkt/examples/rainbow.py
```


9. Create a file to run like the example below:

```bash
> blink.sh

```

10. Open the file and paste the code:

```bash
nano blink.sh

```

```bash
#! /bin/bash

python3 /home/ubuntu/blinkt/examples/rainbow.py 

```


```bash
chmod a+x blink.sh
```

11. Create the file with this path:


```bash
sudo nano /lib/systemd/system/rainbow-leds.service
```

```bash
#systemctl enable rainbow-leds.service

[Unit]
Description=enableHotSpot
After=network.target

[Service]
User=root
Type=forking
ExecStart=/home/ubuntu/blink.sh
StandardOutput=journal

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable rainbow-leds.service
sudo systemctl start rainbow-leds.service
```
### References:

[up-board/up-community](https://github.com/up-board/up-community/wiki/Ubuntu_20.04)

[pimoroni/blinkt](https://github.com/pimoroni/blinkt)
