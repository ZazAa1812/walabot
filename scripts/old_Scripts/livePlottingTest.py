#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np

amp = []
dist = 0

def callback(data):
    amp = data.amplitude
    x = livePlot()
    print x

def livePlot():
    global dist
    dist = dist + 1
    return dist
        
if __name__ == '__main__':
    rospy.init_node('processBscan', anonymous=True)
    rawSignal = rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()