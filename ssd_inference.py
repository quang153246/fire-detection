#!/usr/bin/env python3
#
# This inference reuses sample code published in Nvidia dusty-nv github repo 

import sys
#import argparse
import time
import Jetson.GPIO as GPIO
import cv2
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, Log

input = videoSource("csi://0")

output = videoOutput()
    

net = detectNet(model="models/fire/ssd-mobilenet.onnx", labels="models/fire/labels.txt", input_blob="input_0", output_cvg="scores", 
                    output_bbox="boxes", threshold=0.5)

# process frames until EOS or the user exits
# Led pin for plastic, metal
led_pin11 = 11

# Led pin for garbage

# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(led_pin11, GPIO.OUT, initial=GPIO.LOW)

while True:
    

    # capture the next image
    img = input.Capture()

    if img is None: # timeout
        continue  
        
    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay="box,labels,conf")

    # print the detections
    print("detected {:d} objects in image".format(len(detections)))

    #for detection in detections:
    #    print(detection)

    # render the image
    output.Render(img)
    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format("ssd-mobilenet-v2", net.GetNetworkFPS()))
    
    if (detections):
        print("Fire detected")
        GPIO.output(led_pin11, GPIO.HIGH) 
        print("RED_LED is ON")
    else:
        print("Fire NOT detected")
        print("GREEN_LED is ON")
        GPIO.output(led_pin11, GPIO.LOW)

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break