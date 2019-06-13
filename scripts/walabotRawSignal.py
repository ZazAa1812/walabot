#!/usr/bin/env python
from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import rospy
from std_msgs.msg import Float32MultiArray


modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)

wlbt.Init()

def DataCollect():
     # wlbt.SetArenaX - input parameters
    xArenaMin, xArenaMax, xArenaRes = -10, 10, 0.5
    # wlbt.SetArenaY - input parameters
    yArenaMin, yArenaMax, yArenaRes = -10, 10, 0.5
    # wlbt.SetArenaZ - input parameters
    zArenaMin, zArenaMax, zArenaRes = 5, 11, 0.5

    # Initializes walabot lib
    wlbt.SetSettingsFolder()

    # Establish a connection between the Walabot and the computer
    wlbt.ConnectAny()

    # Set sensor profile
    wlbt.SetProfile(wlbt.PROF_SHORT_RANGE_IMAGING)
    # Set arena by Cartesian coordinates, with arena resolution
    wlbt.SetArenaX(xArenaMin, xArenaMax, xArenaRes)
    wlbt.SetArenaY(yArenaMin, yArenaMax, yArenaRes)
    wlbt.SetArenaZ(zArenaMin, zArenaMax, zArenaRes)
    wlbt.SetThreshold(50)

    # Set filtering to none
    wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_NONE)

    pair = wlbt.GetAntennaPairs()

    # Start the Walabot device
    wlbt.Start()
    # calibrates scanning to ignore or reduce the signals
    # wlbt.StartCalibration()
    # while True:
    #     appStatus, calibrationProcess = wlbt.GetStatus()

    #defining Publisher
    pub = rospy.Publisher('rawSignal', Float32MultiArray, queue_size=4096)
    rospy.init_node('walabotRawSignal', anonymous=True)
    
 
    while not rospy.is_shutdown():
        rospy.sleep(2.0)
        try:
            wlbt.Trigger()
            targets = wlbt.GetSignal((pair[4]))
            # load array into Float32MultiArray form
            rawSignalArray = Float32MultiArray(data=targets)
            pub.publish(rawSignalArray)
            rospy.loginfo(rawSignalArray)
            ### Old publishing ###
            # targets = wlbt.GetSignal((pair[4]))
            # signal = targets[0]
            # timeAxis = targets[1]
            # # rospy.loginfo(signal)funcname
            # pub.publish(signal)
            # # rospy.loginfo(timeAxifuncname
            # pub.publish(timeAxis)
            # rospy.loginfo(numSamples)
            # pub.publish(numSamples)
            # stops Walabot when finished scanning
        except rospy.ROSInterruptException:
            pass

    wlbt.Stop()
    wlbt.Disconnect()
    print("Terminate successfully")

if __name__ == '__main__':
    DataCollect()