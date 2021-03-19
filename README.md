# Raspberry-Pi-Mini-Projects
## Table of Contents
[1. Prerequisite - Setting up the Raspberry Pi]  

#### 1. Prerequisite - Setting up the Raspberry Pi
Before jumping into the projects we must setup the Raspberry Pi correctly. These steps will guide you through setting up SSH, VNC, update to latest software and Pi-Cam which is used in some of these projects.
- Connect a brand new micro sd card any computer running Windows/MacOS etc  
- Install Raspberry Pi Imager using the following [link](https://www.raspberrypi.org/software/)
- Follow the simple on screen instructions on the Raspberry Pi Imager software, once it has completed put the micro sd card in the raspberry pi and connect the pi to power and an external display  
- Connect the pi to an ethernet cable or connect it to a wireless network  
- Go to the preferences and then raspberry pi configuration and enable SSH, VNC, Camera and other settings. Reboot is needed     
- Open the terminal and type ```ipconfig``` and note down the ip address of the pi  
- Install VNC on your computer and enter the pi's ip address to connect remotely. If you see a black screen with a message saying "Cannot display.. " then we have to change some display settings  
- Open terminal in MacOS and type ```ssh pi@192.168.0.94``` (use the correct ip address) and enter the default password ```raspberry```  
- Once you are in the pi terminal, type ```sudo raspi-config``` 
- Navigate to ```Display Options```
- Navigate to ```Resolution```
- Select the resolution of choice (1920 x 1080)
- Reboot
- Now VNC viewer should work correctly
- Now to update the raspberry pi, issue the following commands in the pi terminal
```
sudo apt-get update
```
```
sudo apt-get dist-upgrade
```
This will take some time
- Now to test if the camera is correctly installed and is working correctly. The camera is already enabled in the pi config. Use the following command to snap a picture, it should be saved on the desktop, if it works then everything is fine.
```
raspistill -o Desktop/image-small.jpg -w 640 -h 480
```

