#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
def distanceTrav():
    pub = rospy.Publisher('distanceTurtleTravelled', Int32, queue_size=1000)
    rospy.init_node('distanceTurtle', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    dist = 1
    while not rospy.is_shutdown():
        rospy.loginfo(dist)
        pub.publish(dist)
        rate.sleep()
        dist = dist+1
if __name__ == '__main__':
    try:
        distanceTrav()
    except rospy.ROSInterruptException:
        pass
