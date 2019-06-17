#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def callback(msg):
    global counter
    if counter % 10 == 0:
        #stamp = msg.header.stamp
        #time = stamp.secs + stamp.nsecs * 1e-9
        plt.plot(msg.data)
        plt.axis("equal")
        plt.draw()
        plt.pause(0.00000000001)

    counter += 1
    rospy.loginfo(msg.data)
    #plot.plot()

#def listener():

if __name__ == '__main__':
    counter = 0
    rospy.init_node('process', anonymous=True)
    rospy.Subscriber('rawData', Float32, callback)
    rospy.spin()

