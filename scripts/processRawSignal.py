#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    rospy.loginfo(data.data)

def processRawSignal():
    rospy.init_node('processRawSignal', anonymous=True)
    rospy.Subscriber("rawSignal", Float32MultiArray, callback,queue_size=4096)
    rospy.spin()
        
if __name__ == '__main__':
    processRawSignal()