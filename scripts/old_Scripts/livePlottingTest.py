#!/usr/bin/env python
import rospy
from walabot.msg import signal
import matplotlib.pyplot as plt
import numpy as np

def callback(data):
    amplitude = data.amplitude
    



def livePlot():
    rospy.init_node('processBscan', anonymous=True)
    rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()
        
if __name__ == '__main__':
    livePlot()