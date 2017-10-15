"""
This script runs the RobotManager.WebUI application using a development server.
"""
import ptvsd

from os import environ
from RobotManager_WebUI import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    ptvsd.enable_attach(secret=None,address = ('0.0.0.0', 5072))
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
