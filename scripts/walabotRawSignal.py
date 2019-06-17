#!/usr/bin/env python

from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import rospy
from walabot.msg import rawSignal
import numpy as np

modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)

#Initiate walabot
wlbt.Init()

def DataCollect():
    pair1 = 34
    pair2 = 101
     # wlbt.SetArenaX - input parameters
    xArenaMin, xArenaMax, xArenaRes = -10, 10, 0.5
    # wlbt.SetArenaY - input parameters
    yArenaMin, yArenaMax, yArenaRes = -10, 10, 0.5
    # wlbt.SetArenaZ - input parameters
    zArenaMin, zArenaMax, zArenaRes = 3, 11, 0.5

    # Initializes walabot lib
    wlbt.SetSettingsFolder()

    # Establish a connection between the Walabot and the computer
    wlbt.ConnectAny()

    # Set sensor profile to short range imaging for penetrative scan
    wlbt.SetProfile(wlbt.PROF_SHORT_RANGE_IMAGING)

    # Set arena by Cartesian coordinates, with arena resolution
    wlbt.SetArenaX(xArenaMin, xArenaMax, xArenaRes)
    wlbt.SetArenaY(yArenaMin, yArenaMax, yArenaRes)
    wlbt.SetArenaZ(zArenaMin, zArenaMax, zArenaRes)
    wlbt.SetThreshold(50)

    # Set filtering to none because not using dynamic tracking
    wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_NONE)

    # Get antenna pair list to be use for publishing signal for certain antenna pair
    pair = wlbt.GetAntennaPairs()

    # Start the Walabot device
    wlbt.Start()
    pub = rospy.Publisher('rawSignal', rawSignal, queue_size=100)
    rospy.init_node('walabotRawSignal', anonymous=True)
    
    #Calibrating#
    print("Calibrating")
    # Calibrating pair 1
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background1 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background2 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background3 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background4 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background5 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background6 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background7 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background8 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background9 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair1]))
    background10 = targets[0]
    averagebackgroundpair1 = (np.asarray(background1) + np.asarray(background2) + np.asarray(background3) + np.asarray(background4) + np.asarray(background5) + np.asarray(background6) + np.asarray(background7) + np.asarray(background8) + np.asarray(background9) + np.asarray(background10)) /10 
    
    # Calibrating pair 2
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background1 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background2 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background3 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background4 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background5 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background6 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background7 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background8 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background9 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair2]))
    background10 = targets[0]
    averagebackgroundpair2 = (np.asarray(background1) + np.asarray(background2) + np.asarray(background3) + np.asarray(background4) + np.asarray(background5) + np.asarray(background6) + np.asarray(background7) + np.asarray(background8) + np.asarray(background9) + np.asarray(background10)) /10 

    print("Calibration complete")
 
    while not rospy.is_shutdown():
        rospy.sleep(2.0)
        wlbt.Trigger()
        # Pair 1
        targets1 = wlbt.GetSignal((pair[pair1]))
        tempNewAmplitude1 = np.asarray(targets1[0]) - averagebackgroundpair1
        # Pair 2
        targets2 = wlbt.GetSignal((pair[pair2]))
        tempNewAmplitude2 = np.asarray(targets2[0]) - averagebackgroundpair2
        # Averaging between two pairs
        tempNewAmplitude = (tempNewAmplitude1 + tempNewAmplitude2)/2
        newAmplitude = tempNewAmplitude.tolist()
        # Make raw signal object to contain message
        rawSignalArray = rawSignal()
        rawSignalArray.time = targets[1]
        rawSignalArray.amplitude = newAmplitude
        # Publishing average raw signal data between two pair with background noise remove
        pub.publish(rawSignalArray)
        maxRaw = max(newAmplitude)
        minRaw = min(newAmplitude)
        rospy.loginfo(maxRaw)
        rospy.loginfo(minRaw)

if __name__ == '__main__':
    try:
        DataCollect()
    except KeyboardInterrupt or rospy.ROSInterruptException:
        pass

    wlbt.Stop()
    wlbt.Disconnect()
    print("Terminate successfully")