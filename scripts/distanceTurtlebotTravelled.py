#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
import time
import xlwt
from xlwt import Workbook

temp = []


def move(speed, distance, is_forward):
    global temp
    #declare a Twist message to send velocity commands
    velocity_message = Twist()
    # distance_message = distanceTravelled()
    #get current location 
    if (speed > 0.4):
        print 'speed must be lower than 0.4'
        return

    if (is_forward):
        velocity_message.linear.x =abs(speed)
    else:
        velocity_message.linear.x =-abs(speed)

    distance_moved = 0.0
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    cmd_vel_topic='/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    # distance_publisher = rospy.Publisher('distanceTravelled',distanceTravelled,queue_size=10)
    t0 = rospy.Time.now().to_sec()
 ################ Write data of max amplitude for each scan for depth calibration #################
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0,0, 'Timestamp')
    sheet1.write(0,1, 'Distance')
    i = 1
    while not rospy.is_shutdown():
        rospy.loginfo("Turtlesim moves forwards")
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        t1 =  rospy.Time.now().to_sec()
        # Calculating distance travelled
        distance_moved = (t1-t0) * speed
        distance_moved = round(distance_moved,2)
        temp.append(distance_moved)
        # distance_message.distance = temp
        # distance_publisher.publish(distance_message)
        # print(type(temp))
        rospy.loginfo(t1)
        rospy.loginfo(distance_moved)
        sheet1.write(i,0,t1)
        sheet1.write(i,1,distance_moved) 
        i = i+1         
        if  not (distance_moved<distance):
            rospy.loginfo("reached")
            wb.save('src/walabot/data/dataBscan/distanceTimestamp.xls')
            break
    #finally, stop the robot when the distance is moved
    velocity_message.linear.x =0
    velocity_publisher.publish(velocity_message)

if __name__ == '__main__':
    try:
        rospy.init_node('turtle_motion',anonymous=True)
        rospy.sleep(5)
        move(0.1,0.8,True)
    except rospy.ROSInterruptException or KeyboardInterrupt:
        pass
