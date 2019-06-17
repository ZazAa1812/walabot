#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
import numpy as np
import random

if __name__ =="__main__":
    rospy.init_node("publisher")
    pub = rospy.Publisher('sent_matrix', Float32MultiArray, queue_size=1)
    r = rospy.Rate(0.5)
    i = 0
    j = 0
    # let's build a 3x3 matrix:
    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "amp"
    mat.layout.dim[1].label = "time"
    mat.layout.dim[0].size = 5
    mat.layout.dim[1].size = 5
    mat.layout.data_offset = 0
    num = [[1,2,3,4,5],[1,2,3,4,5]]

    while not rospy.is_shutdown():
        mat.data = num
        pub.publish(mat)
        rospy.loginfo("I'm sending:")
        rospy.loginfo(mat)
        r.sleep()



# # license removed for brevity
# import rospy
# from std_msgs.msg import Float32MultiArray
# from std_msgs.msg import MultiArrayDimension

# def talker():
#     rospy.init_node('talker', anonymous=True)
#     pub = rospy.Publisher('chatter', Float32MultiArray, queue_size=1000)
#     rate = rospy.Rate(10) # 10hz

#     array.layout.dim[0].size = 5
#     array.layout.dim[1].size = 5
#     array.layout.dim[0].stride = 2*5
#     array.layout.dim[1].stride = 3
#     array.layout.data_offset = 0
#     array.data = [0]*10

#     while not rospy.is_shutdown():
#         array = [[1,2,3,4,5],[1,2,3,4,5]]
#         # rows = len(hello_str)
#         # cols = len(hello_str[0])
#         # array = Float32MultiArray(layout=[rows,cols], data=hello_str)#, layout=[rows,cols])
#         pub.publish(array)
#         rospy.loginfo(array)
#         rate.sleep()

# if __name__ == '__main__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass