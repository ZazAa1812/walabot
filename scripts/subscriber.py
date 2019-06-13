#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    rospy.loginfo(data.data.data)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", Float32MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()