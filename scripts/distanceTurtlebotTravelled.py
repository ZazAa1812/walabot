#!/usr/bin/env python
import rospy
from walabot.msg import distanceTravelled
val = []
temp = 0
def distanceTrav():
    global val,temp
    pub = rospy.Publisher('distanceTurtleTravelled', distanceTravelled, queue_size=1000)
    rospy.init_node('distanceTurtle', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    dist = distanceTravelled()
    while not rospy.is_shutdown():
        val.append(temp)
        dist.distance = val
        rospy.loginfo(dist)
        pub.publish(dist)
        rate.sleep()
        temp = temp+1

if __name__ == '__main__':
    try:
        distanceTrav()
    except rospy.ROSInterruptException:
        pass
