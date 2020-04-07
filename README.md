# first-robot-project
Project uses Raspberry-pi Model B, arduino and motor controller for controlling very basic Robot.
Robot sees by webcam connected to Raspberry.
On Raspberry there is installed linux Raspbian with Python and lighthttp server.
Web application created using python language and flask framework, deployed with FastCgi are used for control the direction of robot, with buttons:
- Forward
- Left
- Right
- Backward
- Stop

Web application shows the image captured from Webcam using OpenCV and showed on page with base64 conversion.

Raspberry-pi are connected with arduino using I2C interface.
Arduino controls the motors.




