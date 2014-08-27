#!/usr/bin/env python

import os
import time
import BaseHTTPServer

HOST_NAME = os.getenv("OPENSHIFT_DIY_IP")
PORT_NUMBER = 8080

class MaintenanceHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.curDir = os.path.dirname(os.path.realpath(__file__))

        if self.path=="/":
            self.path = "/503.html"
        # If requested file does not exists, show 503 page
        elif os.path.exists(self.curDir+self.path) == False:
            self.path = "/503.html"

        try:
            # Check extensions and set the mime type accordingly
            sendReply = False

            if self.path.endswith(".html"):
                mimetype    = "text/html"
                sendReply   = True
            if self.path.endswith(".png"):
                mimetype    = "image/png"
                sendReply   = True
            if self.path.endswith(".jpg"):
                mimetype    = "image/jpg"
                sendReply   = True
            if self.path.endswith(".gif"):
                mimetype    = "image/gif"
                sendReply   = True
            if self.path.endswith(".js"):
                mimetype    = "application/javascript"
                sendReply   = True
            if self.path.endswith(".css"):
                mimetype    = "text/css"
                sendReply   = True


            if sendReply == True:
                # Open the static file requested and send it
                f = open(self.curDir+self.path)
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()

            return
        except IOError:
            self.send_error(404, 'File not found: %s' % self.path)

if __name__ == '__main__':
   server_class = BaseHTTPServer.HTTPServer
   httpd = server_class((HOST_NAME, PORT_NUMBER), MaintenanceHandler)
   print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
   try:
      httpd.serve_forever()
   except KeyboardInterrupt:
      pass
   httpd.server_close()
   print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
