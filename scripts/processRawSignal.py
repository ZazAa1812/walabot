#!/usr/bin/env python
import rospy
from walabot.msg import rawSignal

def callback(data):
    rospy.loginfo(data.time)

def processRawSignal():
    rospy.init_node('processRawSignal', anonymous=True)
    rospy.Subscriber("rawSignal", rawSignal, callback)
    rospy.spin()
        
if __name__ == '__main__':
    processRawSignal()