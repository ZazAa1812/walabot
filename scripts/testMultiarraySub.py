#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
import numpy as np

def callback(data):
    dstride0 = data.layout.dim[0].stride
    dstride1 = data.layout.dim[1].stride
    h = data.layout.dim[0].size
    w = data.layout.dim[0].size
    x = data.data[0+dstride1*0]
    rospy.loginfo(x)
    xy = data.data
    rospy.loginfo(xy)

if __name__ =="__main__":
    rospy.init_node("subscriber")
    rospy.Subscriber("sent_matrix", Float32MultiArray, callback)
    rospy.spin()
