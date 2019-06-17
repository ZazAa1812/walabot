#!/usr/bin/env python
import rospy
from walabot.msg import rawSignal
import matplotlib.pyplot as plt
import numpy as np
from walabot.msg import processData

def callback(data):
    amplitude = data.amplitude
    timeAxis = data.time  
    rospy.loginfo(amplitude) 


def processAscan():
    rospy.init_node('processAscan', anonymous=True)
    rospy.Subscriber("processedAbsAscanData", processData, callback)
    rospy.spin()
        
if __name__ == '__main__':
    processAscan()