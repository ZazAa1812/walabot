#!/usr/bin/env python
from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import rospy
from walabot.msg import signal
import numpy as np

modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)
i = 0
depth = 0
#Initiate walabot
wlbt.Init()

def DataCollect():
    global i,depth
    pair1 = 34
    pair2 = 101
    # depth1 = 0.0119371      #Depth 0cm which is 2.5cm from Walabot that is separated by a medium
    # depth2  = 0.00570357    #Depth 2.5cm
    # depth3  = 0.00488826    #Depth 5.0cm
    # depth4  = 0.00346715    #Depth 7.5cm
    # d1 = 0
    # d2 = 2.5
    # d3 = 5.0
    # d4 = 7.5
     # wlbt.SetArenaX - input parameters
    xArenaMin, xArenaMax, xArenaRes = -10, 10, 0.5
    # wlbt.SetArenaY - input parameters
    yArenaMin, yArenaMax, yArenaRes = -10, 10, 0.5
    # wlbt.SetArenaZ - input parameters
    zArenaMin, zArenaMax, zArenaRes = 2.5, 13, 0.5

    # Initializes walabot lib
    wlbt.SetSettingsFolder()

    # Establish a connection between the Walabot and the computer
    wlbt.ConnectAny()

    # Set sensor profile to short range imaging for penetrative scan
    wlbt.SetProfile(wlbt.PROF_SHORT_RANGE_IMAGING)
    wlbt.SetAdvancedParameter(wlbt.PARAM_DIELECTRIC_CONSTANT,1)
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
    pub = rospy.Publisher('rawSignal', signal, queue_size=100)
    rospy.init_node('walabotRawSignal', anonymous=True)
    
    ################Calibrating#######################
    print("Calibrating")
    # # Calibrating pair 1
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
    ###########End Calibration########
    
    ###########Main Function##########
    while not rospy.is_shutdown():
        rospy.sleep(1)
        wlbt.Trigger()
        targets = wlbt.GetSignal((pair[pair1]))
        # Pair 1
        targets1 = wlbt.GetSignal((pair[pair1]))
        tempNewAmplitude1 = np.asarray(targets1[0]) - averagebackgroundpair1
        # Pair 2
        targets2 = wlbt.GetSignal((pair[pair2]))
        tempNewAmplitude2 = np.asarray(targets2[0]) - averagebackgroundpair2
        # Averaging between two pairs data
        tempNewAmplitude = (tempNewAmplitude1 + tempNewAmplitude2)/2
        newAmplitude = tempNewAmplitude.tolist()
        #######Experiment 1: Depth Calculation##########
        valAmp = max(tempNewAmplitude)
        indexx = newAmplitude.index(valAmp)
        t = np.asarray(targets[1])
        t = t[indexx]
        print("##################Data Starts Here##################")
        print("Index")
        print(indexx)
        print("Max Amplitude")
        print (valAmp)
        print("Time")
        print (t)

        ####
        # if valAmp <= depth1 and valAmp > depth2:
        #     depth = ((valAmp - depth1)*d2 + (valAmp-depth2)*d1)/(depth2 - depth1)
        # elif valAmp <= depth2 and valAmp > depth3:
        #     depth = ((valAmp - depth2)*d3 + (valAmp-depth3)*d2)/(depth3 - depth2)
        # elif valAmp <= depth3 and valAmp > depth4:
        #     depth = ((valAmp - depth3)*d4 + (valAmp-depth4)*d3)/(depth4 - depth3)
        # else:
        #     depth = 0
        #####
        # if valAmp <= depth1 and valAmp > depth2:
        #     a = -2.5*(0.0119371-valAmp)
        #     b = -0.00623353
        #     c = a/b
        #     depth = c
        # elif valAmp <= depth2 and valAmp > depth3:
        #     a = -2.5
        # elif valAmp <= depth3 and valAmp > depth4:
        #     a = 0.00142111
        #     b = (depth3 - valAmp)
        #     c = - 2.5 * b
        #     d = c - (a*2.5)
        #     e = (d - (a*2.5))
        #     depth = e/-a
        # else:
        #     depth = 0

        # print("Depth")
        # print (depth)
        ################################################
        # Make raw signal object to contain message
        rawSignalArray = signal()
        rawSignalArray.time = targets[1]
        rawSignalArray.amplitude = newAmplitude
        # Publishing average raw signal data between two pair with background noise remove
        pub.publish(rawSignalArray)
        # print("Publishing raw signal data")
        # print (i)
        targets1 = []
        targets2 = []
        targets = []
        newAmplitude = []
        i = i + 1

if __name__ == '__main__':
    try:
        DataCollect()
    except KeyboardInterrupt or rospy.ROSInterruptException:
        pass

    wlbt.Stop()
    wlbt.Disconnect()
    print("Terminate successfully")