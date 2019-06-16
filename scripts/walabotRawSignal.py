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
    #number of antenna
    ant = 1
    #Declare background and summation zero array for calibration
    background = []
    summation = []
    newAmplitude = [[0]] * ant
    signal_list = [[0]] * ant
    #Antenna pair number
    num = 4

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
    
    # Calibrating based on DataCollection code by People and Fall Detection, https://www.hackster.io/42748/people-and-fall-detection-with-walabot-8db4aa
    # Will be updated later
    print("Calibrating")
    for i in range(10):
        wlbt.Trigger()
        targets = wlbt.GetSignal((pair[num]))
        background.append(targets[0])
    background = np.asarray(background)
    summation.append(background[0] + background[0 + ant] + background[0 + (ant * 2)] + background[0 + (ant * 3)] + background[0 + (ant * 4)] + background[0 + (ant * 5)] + background[0 + (ant * 6)] + background[0 + (ant * 7)] + background[0 + (ant * 8)] + background[0 + (ant * 9)])
    summation = np.asarray(summation)
    averageBackground = summation/10
    print("Calibration Complete")

    #Processing rawData by removing background noise and publish the data
    while not rospy.is_shutdown():
        rospy.sleep(2.0)
        wlbt.Trigger()
        del signal_list[0:ant]
        targets = wlbt.GetSignal((pair[num]))
        signal_list.append(targets[0])
        newAmplitude = signal_list - averageBackground
        print(newAmplitude)
        rawSignalArray = rawSignal()
        rawSignalArray.time = targets[1]
        rawSignalArray.amplitude = newAmplitude
        pub.publish(rawSignalArray)
        #rospy.loginfo(rawSignalArray.amplitude)

if __name__ == '__main__':
    try:
        DataCollect()
    except KeyboardInterrupt or rospy.ROSInterruptException:
        pass

    wlbt.Stop()
    wlbt.Disconnect()
    print("Terminate successfully")