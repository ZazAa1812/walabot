#!/usr/bin/env python

import rospy
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('yo', String, queue_size=1000)
    rospy.init_node('hey', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        hello_str = "%s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
