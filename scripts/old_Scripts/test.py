#!/usr/bin/env python
from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import rospy
from std_msgs.msg import Float32MultiArray
import threading
from time import sleep


modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)

wlbt.Init()

def callback(data):
    req_lock.acquire()
    print (data.data)
    req_lock.release()

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

    #defining Publisher
    pub = rospy.Publisher('rawSignal', Float32MultiArray, queue_size=1000)
    
    # while not rospy.is_shutdown():
    wlbt.Trigger()
    targets = wlbt.GetSignal((pair[4]))
    rawSignalArray = Float32MultiArray(data=targets)
    pub.publish(rawSignalArray)
    rospy.loginfo(rawSignalArray)
    wlbt.Stop()  # stops Walabot when finished scanning
    


if __name__ == '__main__':
    # try:
    while not rospy.is_shutdown():
        req_lock = threading.Lock()
        rospy.init_node('walabotRawSignal', anonymous=True)
        # rate = rospy.Rate(1) #10Hz
        DataCollect()
        # rate.sleep()
        # rospy.Subscriber("rawSignal", Float32MultiArray, callback)
    #     rospy.spin()
    # except rospy.ROSInterruptException:
    #     pass

    wlbt.Disconnect()

    print("Terminate successfully")