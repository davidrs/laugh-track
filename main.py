#!/usr/bin/env python
import os
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


class MyHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        print "path: " + path

        if path == "/laugh":
            self.play_laugh()

        elif path == "/todo":
            print "TODO: any action we want."

        else:
            print "Unkown command: " + path


	    # default root -> cwd        
        root = os.getcwd()
        # return unchanged path to get any appropriate files.
        return os.path.join(root, path)

    # Plays a laugh track.     
    def play_laugh(self):
        print "TODO: play laugh audio"




# This code will only run if this file is run as the main python file.
if __name__ == '__main__':
    print "Start server"
    httpd = HTTPServer(('0.0.0.0', 8000), MyHandler)
    httpd.serve_forever()
    print "Code here and below won't run."
