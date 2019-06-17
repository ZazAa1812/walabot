#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
def distanceTrav():
    pub = rospy.Publisher('distanceTbotTravelled', Int32, queue_size=1000)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    hello_str = 1
    while not rospy.is_shutdown():
        
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        hello_str = hello_str+1
if __name__ == '__main__':
    try:
        distanceTrav()
    except rospy.ROSInterruptException:
        pass
