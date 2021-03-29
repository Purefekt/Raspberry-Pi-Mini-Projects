# Raspberry-Pi-Mini-Projects
Please open a new issue if you find any bugs so i can fix them.
## Table of Contents
1. [Prerequisite - Setting up the Raspberry Pi](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects/blob/main/README.md#1-prerequisite---setting-up-the-raspberry-pi)  
2. [Displaying my name on SenseHAT](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects/blob/main/README.md#2-displaying-my-name-on-sensehat)
3. [Display a smiley face on the SenseHAT](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects/blob/main/README.md#3-display-a-smiley-face-on-the-sensehat)
4. [Interacting with the joystick on SenseHAT](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects/blob/main/README.md#4-interacting-with-the-joystick-on-sensehat)
5. [Electronic dice using SenseHAT](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects/blob/main/README.md#5-electronic-dice-using-sensehat)
6. [Logging current temperature, pressure, humidity](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#6-logging-current-temperature-pressure-humidity)
7. [Plotting a graph of current temp, humidity and pressure](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#7-plotting-a-graph-of-current-temp-humidity-and-pressure)
8. [Predicting the altitude](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#8-predicting-the-altitude)
9. [Detects the pi's pitch, roll and yaw](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#9-detects-the-pis-pitch-roll-and-yaw)
10. [8 point compass](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#10-8-point-compass)
11. [Traffic light with sync button](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#11-traffic-light-with-sync-button)
12. [Catch the ball game](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#12-catch-the-ball-game)
13. [Simplified pong game](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#12-catch-the-ball-game)
14. [Snake game](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#14-snake-game)
15. [Capture and display images using OpenCV and Pi cam](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#15-capture-and-display-images-using-opencv-and-pi-cam)
16. [Accessing Pi Cam video stream with OpenCV](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#16-accessing-pi-cam-video-stream-with-opencv)
16. [Motion Detection](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#17-motion-detection)

### 1. Prerequisite - Setting up the Raspberry Pi
Before jumping into the projects we must setup the Raspberry Pi correctly. These steps will guide you through installing Raspbian onto an Micro SD card, SSH, VNC, update to latest software and Pi-Cam which is used in some of these projects.
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

### 2. Displaying my name on SenseHAT
We need a SenseHAT connected to the Raspberry pi. This python script will display the letters V,E,E,R one by one on the LED matrix. It can be changed to display any string of characters.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 3. Display a smiley face on the SenseHAT
We need a SenseHAT connected to the Raspberry pi. This python script will display a simley face on the LED matrix. The code can be changed to display any image on a 8x8 matrix.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 4. Interacting with the joystick on SenseHAT
We need a SenseHAT connected to the Raspberry pi. The LED matrix will display different colors based on which direction is pressed on the joystick.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 5. Electronic dice using SenseHAT
We need a SenseHAT connected to the Raspberry pi. When pressing down on the joystick, the LED matrix will display a randomly chosen number as shown on a dice of 6 sides.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 6. Logging current temperature, pressure, humidity
We need a senseHAT connected to the Raspberry pi. Running the script logs the current temperature, pressure and humidity in intervals of 1 second.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 7. Plotting a graph of current temp, humidity and pressure
We need a senseHAT connected to the Raspberry pi. This script will collect the current temperature, humidity and pressure for 5 seconds with intervals of 0.5 seconds and plot a graph using the Matplotlib library.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 8. Predicting the altitude
We need a senseHAT connected to the Raspberry pi. This script collects the atmospheric pressure and approximates the altitude.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 9. Detects the pi's pitch, roll and yaw
We need a senseHAT connected to the Raspberry pi. This script tells us the orientation of the raspberry pi by calculating its pitch, roll and yaw.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 10. 8 point compass
We need a senseHAT connected to the Raspberry pi. After callibration this script is able to detect the magnetic direction and displays it on the LED matrix. This is an 8 point compass so the 8 directions are N, NE, E, SE, S, SW, W, NW.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 11. Traffic light with sync button
We need a senseHAT connected to the Raspberry pi. This scripts immitates a traffic light and shows Green, Read and Yellow on the LED Matrix. If there are multiple such "Traffic Lights" they can be synchronised by pressing the middle button.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 12. Catch the ball game
We need a senseHAT connected to the Raspberry pi. This scripts lets the user play catch the ball game on the LED matrix. We have a 2x1 bar at the bottom which we can move right or left using the joystick. A ball will appear from top and the objective is to catch the ball. If the ball falls off the the player loses and the final score is displayed on the LED matrix.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 13. Simplified pong game
We need a senseHAT connected to the Raspberry pi. This script lets the user play the pong game on the LED matrix. A ball will appear, the user has to bounce it off the pad which can be moved right and left with the joystick and prevent it from falling to the ground. Once the ball strikes the ground the game is over and the final score is displayed on the LED matrix.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 14. Snake game
We need a senseHAT connected to the Raspberry pi. This script lets the user play the Snake game on the sense hat. It starts with snake of size 1 and the user must guide it to the food(red led), everytime the snake eats food the snake grows by 1. But if the snake's head (leading led) crosses over any part of its body, the game is over and it restarts. Also as the length of the snake grows, the speed of the snake increases.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 15. Capture and display images using OpenCV and Pi cam.
We need the Pi Cam v2 module for this. This script shows a stream of images using OpenCV which are being captured by the Pi cam.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 16. Accessing Pi Cam video stream with OpenCV.
We need the Pi Cam v2 module for this. This script lets us use OpenCV library to access the video stream of the Pi cam.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)

### 17. Motion Detection
We need the Pi Cam v2 module for this. This script lets us see if there is any change in the current video stream. When there is a change in the frame, a flag saying "New object" is shown on screen.
[Go up](https://github.com/Purefekt/Raspberry-Pi-Mini-Projects#table-of-contents)