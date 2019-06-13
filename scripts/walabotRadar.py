#!/usr/bin/env python
from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import rospy
from std_msgs.msg import Float32

modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)

wlbt.Init()

def DataCollect():
    wlbt.SetSettingsFolder()
    # Establish a connection between the Walabot and the computer
    wlbt.ConnectAny()
    # Set sensor profile to short-range penetrative scanning dielectric materials
    wlbt.SetProfile(wlbt.PROF_SHORT_RANGE_IMAGING)
    # Set filtering to none
    wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_NONE)
    wlbt.Start()

    pub = rospy.Publisher('rawData', Float32, queue_size=1000)
    rospy.init_node('radar', anonymous=True)
    rate = rospy.Rate(30) #10Hz
    pair = wlbt.GetAntennaPairs()
    while not rospy.is_shutdown():
        wlbt.Trigger()
        targets = wlbt.GetSignal((pair[0]))
        #signal = 3.54;
        signal = targets[0]
        #timeAxis = targets[1]
        #rospy.loginfo(signal)
        #rospy.loginfo(111111111111111111111111111)
        #rospy.loginfo(signal[0])

        for i in range(len(signal)):
            rospy.loginfo(signal[i])
            pub.publish(signal[i])
            #rospy.loginfo(timeAxis[i])
            #pub.publish(timeAxis[i])
            #for k in range(ant):
        rate.sleep()


if __name__ == '__main__':
    try:
        DataCollect()
    except rospy.ROSInterruptException:
        pass

    wlbt.Stop()  # stops Walabot when finished scanning
    wlbt.Disconnect()

    print("Terminate successfully")