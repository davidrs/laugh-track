#!/usr/bin/env python
import os
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

# Our libs
import audio


class MyHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        print "path: " + path

        if path == "/laugh":
            audio.play_laugh()

        elif path == "/todo":
            print "TODO: any action we want."

        else:
            print "Unkown command: " + path


	    # default root -> cwd        
        #root = os.getcwd()
        #print root
        # return unchanged path to get any appropriate files.
        return path[1:]



# This code will only run if this file is run as the main python file.
if __name__ == '__main__':
    print "Start server"
    httpd = HTTPServer(('0.0.0.0', 8000), MyHandler)
    httpd.serve_forever()
    print "Code here and below won't run."
