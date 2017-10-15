import cv2
import base64 #POCO PERFORMANTE
#from codecs import encode
import smbus
from RobotManager_WebUI.utils import StopWatch
from RobotManager_WebUI.utils import Converter
import logging
from RobotManager_WebUI import app
from RobotManager_WebUI import cameraRef
from RobotManager_WebUI import bus
from flask import request
from flask import Response



@app.route('/image/<int:timestamp>')
def get_image(timestamp):
    #sw = StopWatch()
    conv = Converter()
    #sw.start()
    retval,im = cameraRef.read()
    if not retval: return "0"
    #logging.info("CAPTURE Elapsed: %d",sw.elapsed())
    img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #sw.reset()
    #sw.start()
    cnt = cv2.imencode('.jpg',img)[1]
    #logging.info("ENCODING Elapsed: %d",sw.elapsed())

    #sw.reset()
    #sw.start()
    cnt_str = cnt.tostring()
    #logging.info("TOSTRING Elapsed: %d",sw.elapsed())

    #sw.reset()
    #sw.start()
    #b64 = base64.encodestring(cnt_str)
    #b64 = base64.encodebytes(cnt.ravel())
    #b64 = encode(cnt.ravel(),'base64')
    #b64 = conv.toBae64Np(cnt)
    b64 = conv.encodeBase64(cnt_str);
    #logging.info("BASE64 Elapsed: %d",sw.elapsed())

    return b64

@app.route('/move',methods=["POST"])
def set_move():
    DEVICE_ADDRESS = 0x8
    direction=request.json["direction"]
    value = request.json["value"]
    if direction == 1:
        bus.write_byte_data(DEVICE_ADDRESS, ord('F'), int(value))
    elif direction == 2:
        bus.write_byte_data(DEVICE_ADDRESS, ord('B'), int(value))
    elif direction == 3:
        bus.write_byte_data(DEVICE_ADDRESS, ord('R'), int(value))
    elif direction == 4:
        bus.write_byte_data(DEVICE_ADDRESS, ord('L'), int(value))
    else:
        bus.write_byte_data(DEVICE_ADDRESS, ord('S'), int(value))
    return Response(status=200)
