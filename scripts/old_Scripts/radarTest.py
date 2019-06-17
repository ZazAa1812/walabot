#!/usr/bin/env python
from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import rospy
from std_msgs.msg import Float32
import numpy as np

modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)
wlbt.Init()

def DataCollect():
    wlbt.SetSettingsFolder()
    # Establish a connection between the Walabot and the computer
    wlbt.ConnectAny()
    # Set sensor profile
    wlbt.SetProfile(wlbt.PROF_SENSOR)
    # Set filtering to none
    wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_NONE)
    wlbt.Start()

    

    pub = rospy.Publisher('rawData', Float32, queue_size=10)
    rospy.init_node('radar', anonymous=True)

# ________________________________________________________________________________________________________
    # |                                                 CALIBRATION                                            |
    # | _______________________________________________________________________________________________________|
    # Scans the arena 10 times and takes the average of those scans for the background signals' frame
    ant = 40
    pair = wlbt.GetAntennaPairs()
    background = []
    summation = []
    print("Calibrating")
    # Lets the user know calibration has begun

    for i in range(30):
        wlbt.Trigger()
        for num in range(ant):
            targets = wlbt.GetSignal((pair[1]))
            background.append(targets[0])

    background = np.asarray(background)

    for i in range(ant):
        summation.append(
            background[i] + background[i + ant] + background[i + (ant * 2)] + background[i + (ant * 3)] + background[
                i + (ant * 4)] +
            background[i + (ant * 5)] + background[i + (ant * 6)] + background[i + (ant * 7)] + background[i + (ant * 8)] +
            background[i + (ant * 9)])

    summation = np.asarray(summation)
    average_background = summation / 10

    print("Calibration Complete")


    
    rate = rospy.Rate(1) #10Hz
    
    while not rospy.is_shutdown():
        #wlbt.Trigger()
        #targets = wlbt.GetSignal((pair[1]))
        #signal = 3.54;
        for num in range(ant):
            targets = wlbt.GetSignal((pair[num]))
            signal = targets[0]
        #timeAxis = targets[1]
        #rospy.loginfo(signal)
        #rospy.loginfo(111111111111111111111111111)
        #rospy.loginfo(signal[0])

        for i in range(len(signal)):
            rospy.loginfo(signal[i]*10)
            pub.publish(signal[i]*10)
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