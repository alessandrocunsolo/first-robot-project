"""
The flask application package.
"""


import cv2
import logging
import smbus
from flask import Flask


logging.basicConfig(filename="/home/pi/sitelogs.log",level=logging.DEBUG,format='%(asctime)s %(message)s')
app = Flask(__name__)
bus = smbus.SMBus(1)

cameraRef = cv2.VideoCapture(0)

import RobotManager_WebUI.utils
import RobotManager_WebUI.views
import RobotManager_WebUI.restservice

