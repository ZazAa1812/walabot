#!/usr/bin/env python
from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import rospy
from walabot.msg import signal
import numpy as np
# import xlwt
# from xlwt import Workbook

modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)
i = 0
depth = 0
j = 0
#Initiate walabot
wlbt.Init()

def DataCollect():
    global i,depth,j
    #antenna pair
    pair1 = 2   # 1 -> 4
    pair2 = 34  # 5 -> 8
    pair3 = 66  # 12 -> 9
    pair4 = 101 # 16 -> 15
    pair5 = 135 # 18 -> 17

    ########## Depth Estimation Value ##############
    # Uncomment only when running depth
    depth1 = 0.0256278951      #Depth 0cm which is 2.5cm from Walabot that is separated by a medium
    depth2  = 0.0083904274    #Depth 2cm
    depth3  = 0.0052663876   #Depth 4.0cm
    depth4  = 0.0050545808   #Depth 6.0cm
    depth5  = 0.002128544   #Depth 8.0cm
    d1 = 0
    d2 = 2
    d3 = 4
    d4 = 6
    d5 = 8
    ########### End #############
     # wlbt.SetArenaX -34input parameters
    xArenaMin, xArenaMax, xArenaRes = -10, 10, 0.5
    # wlbt.SetArenaY - 34nput parameters
    yArenaMin, yArenaMax, yArenaRes = -10, 10, 0.5
    # wlbt.SetArenaZ - 34nput parameters
    zArenaMin, zArenaMax, zArenaRes = 2.5, 14, 0.5

    # Initializes walab34t lib
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

    # Calibrating pair 3
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background1 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background2 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background3 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background4 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background5 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background6 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background7 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background8 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair3]))
    background9 = targets[0]
    wlbt.Trigger() 
    targets = wlbt.GetSignal((pair[pair3]))
    background10 = targets[0]
    averagebackgroundpair3 = (np.asarray(background1) + np.asarray(background2) + np.asarray(background3) + np.asarray(background4) + np.asarray(background5) + np.asarray(background6) + np.asarray(background7) + np.asarray(background8) + np.asarray(background9) + np.asarray(background10)) /10 

    # Calibrating pair 4
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background1 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background2 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background3 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background4 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background5 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background6 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background7 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background8 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background9 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair4]))
    background10 = targets[0]
    averagebackgroundpair4 = (np.asarray(background1) + np.asarray(background2) + np.asarray(background3) + np.asarray(background4) + np.asarray(background5) + np.asarray(background6) + np.asarray(background7) + np.asarray(background8) + np.asarray(background9) + np.asarray(background10)) /10 

    # Calibrating pair 5
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background1 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background2 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background3 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background4 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background5 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background6 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background7 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background8 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background9 = targets[0]
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[pair5]))
    background10 = targets[0]
    averagebackgroundpair5 = (np.asarray(background1) + np.asarray(background2) + np.asarray(background3) + np.asarray(background4) + np.asarray(background5) + np.asarray(background6) + np.asarray(background7) + np.asarray(background8) + np.asarray(background9) + np.asarray(background10)) /10 

    print("Calibration complete")
    rospy.sleep(5)
    ###########End Calibration########
    
    ###########Main Function##########
    while not rospy.is_shutdown():
        rospy.sleep(0.05)
        wlbt.Trigger()
        targets = wlbt.GetSignal((pair[pair2]))
        # # Pair 1
        targets1 = wlbt.GetSignal((pair[pair1]))
        tempNewAmplitude1 = np.asarray(targets1[0]) - averagebackgroundpair1
        # Pair 2
        targets2 = wlbt.GetSignal((pair[pair2]))
        tempNewAmplitude2 = np.asarray(targets2[0]) - averagebackgroundpair2
        # Pair 3
        targets3 = wlbt.GetSignal((pair[pair3]))
        tempNewAmplitude3 = np.asarray(targets3[0]) - averagebackgroundpair3
        # Pair 4
        targets4 = wlbt.GetSignal((pair[pair4]))
        tempNewAmplitude4 = np.asarray(targets4[0]) - averagebackgroundpair4
        # Pair 5
        targets5 = wlbt.GetSignal((pair[pair5]))
        tempNewAmplitude5= np.asarray(targets5[0]) - averagebackgroundpair5

        # Averaging between 2 and 5 pairs data
        # tempNewAmplitude = (tempNewAmplitude2 + tempNewAmplitude4)/2
        tempNewAmplitude = (tempNewAmplitude1 + tempNewAmplitude2+tempNewAmplitude3+tempNewAmplitude4+tempNewAmplitude5)/5
        newAmplitude = tempNewAmplitude.tolist()

        #######Experiment 1: Depth Calculation###########
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

        ################ Write data of max amplitude for each scan for depth calibration #################
        # if i == 0:
        #     wb = Workbook()
        #     sheet1 = wb.add_sheet('Sheet 1')
        #     # sheet1.write(0,0, 'Number of Scan')
        #     sheet1.write(0,1, 'Depth')
        #     # sheet1.write(0,1, 'Signal Amplitude')
        #     # sheet1.write(0,2, 'Time (ns)')
        #     # sheet1.write(0,3, 'Data Index')
        #     i = i + 1
        # sheet1.write(i,0,i)
        # sheet1.write(i,1,valAmp)
        # sheet1.write(i,2,t)
        # sheet1.write(i,3,indexx)   
        
        #############################################################################################################

        ################# Depth estimation ##################################
        if valAmp <= depth1 and valAmp > depth2:
            depth = ((valAmp - depth1)*d2 + (valAmp-depth2)*d1)/(depth2 - depth1)
        elif valAmp <= depth2 and valAmp > depth3:
            depth = ((valAmp - depth2)*d3 + (valAmp-depth3)*d2)/(depth3 - depth2)
        elif valAmp <= depth3 and valAmp > depth4:
            depth = ((valAmp - depth3)*d4 + (valAmp-depth4)*d3)/(depth4 - depth3)
        elif valAmp <= depth4 and valAmp > depth5:
            depth = ((valAmp - depth4)*d5 + (valAmp-depth5)*d4)/(depth5 - depth4)
        else:
            depth = 0

        print("Depth")
        print (depth)
        # sheet1.write(i,1,depth) 
        #########################End######################################

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
        targets3 = []
        targets4 = []
        targets5 = []
        targets = []
        newAmplitude = []
        i = i + 1
        # j = j + 1
        # if j==50:
        #     ishut = "shutdown"
        #     wb.save('src/walabot/data/depthcalibration/fiveAnt/6cmMd.xls')
        #     rospy.signal_shutdown(ishut)

if __name__ == '__main__':
    try:
        DataCollect()
    except KeyboardInterrupt or rospy.ROSInterruptException:
        pass

    wlbt.Stop()
    wlbt.Disconnect()
    print("Terminate successfully")