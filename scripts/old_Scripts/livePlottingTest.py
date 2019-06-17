#!/usr/bin/env python
import rospy
from walabot.msg import signal
from std_msgs.msg import Int32
import matplotlib.pyplot as plt
import numpy as np
import message_filters


def callback(rawSignal, distance):
    x = rawSignal.amplitude

def livePlot():
    rospy.init_node('processBscan', anonymous=True)
    rawSignal = rospy.Subscriber("rawSignal", signal)
    distance = rospy.Subscriber("distanceTurtleTravelled", Int32)
    ts = message_filters.TimeSynchronizer([rawSignal, distance],10)
    ts.registerCallback(callback)
    rospy.spin()
        
if __name__ == '__main__':
    livePlot()