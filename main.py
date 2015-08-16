#!/usr/bin/env python
import os
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import time
import RPi.GPIO as GPIO


# Our libs
import audio
import rf

class MyHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        print "path: " + path

        if path == "/laugh":
            audio.play_laugh()

        elif path == "/5-on":
	    print "on 5"
	    rf.on(5)
        elif path == "/5-off":
	    print "5 off"
	    rf.off(5)
        elif path == "/todo":
            print "TODO: any action we want."

        else:
            print "Unkown command: " + path


	    # default root -> cwd        
        #root = os.getcwd()
        #print root
        # return unchanged path to get any appropriate files.
        return path[1:]

def buttonEvent(pin):
    audio.play_laugh()




# This code will only run if this file is run as the main python file.
if __name__ == '__main__':
    print "Setup hardware interrupts."
    # tell the GPIO module that we want to use 
    # the chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(7,GPIO.IN)
    # tell the GPIO library to look out for an 
    # event on pin 23 and deal with it by calling 
    # the buttonEventHandler function
    GPIO.add_event_detect(7,GPIO.RISING)
    GPIO.add_event_callback(7,buttonEvent,100)



    print "Start server"
    httpd = HTTPServer(('0.0.0.0', 8000), MyHandler)
    httpd.serve_forever()
    print "Code here and below won't run."
