#!/usr/bin/env python

import rospy
from std_msgs.msg import String
def distanceTrav():
    pub = rospy.Publisher('distanceTbotTravelled', String, queue_size=1000)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        hello_str = "%s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        distanceTrav()
    except rospy.ROSInterruptException:
        pass
