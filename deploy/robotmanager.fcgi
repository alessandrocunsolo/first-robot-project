#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from RobotManager_WebUI  import app
from werkzeug.contrib.fixers import LighttpdCGIRootFix

if __name__ == '__main__':
    #WSGIServer(app,bindAddress='/tmp/robotmanager-fcgi.sock').run()
    app = LighttpdCGIRootFix(app,app_root='/')
    WSGIServer(app).run()
