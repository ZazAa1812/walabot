#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
import numpy as np

import random

import numpy as np

if __name__ =="__main__":
    rospy.init_node("publisher")
    pub = rospy.Publisher('sent_matrix', Float32MultiArray, queue_size=1)
    r = rospy.Rate(0.5)
    # let's build a 3x3 matrix:
    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "height"
    mat.layout.dim[1].label = "width"
    mat.layout.dim[0].size = 3
    mat.layout.dim[1].size = 3
    mat.layout.dim[0].stride = 3*3
    mat.layout.dim[1].stride = 3
    mat.layout.data_offset = 0
    mat.data = [0]*9

    # save a few dimensions:
    dstride0 = mat.layout.dim[0].stride
    dstride1 = mat.layout.dim[1].stride
    offset = mat.layout.data_offset
    while not rospy.is_shutdown():
        tmpmat = np.zeros((3,3))
        for i in range(3):
            for j in range(3):
                num = random.randrange(0,10)
                mat.data[offset + i + dstride1*j] = num
                tmpmat[i,j] = num
        pub.publish(mat)
        rospy.loginfo("I'm sending:")
        rospy.loginfo(mat)
        r.sleep()