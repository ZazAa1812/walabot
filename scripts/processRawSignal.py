#!/usr/bin/env python
import rospy
from walabot.msg import rawSignal
import matplotlib.pyplot as plt
import numpy as np

def callback(data):
    signalAxis = data.amplitude
    timeAxis = data.time
    # rospy.loginfo(data.amplitude)
    temp = abs(np.asarray(signalAxis))
    absSignal = temp.tolist()
    plt.clf()
    # plt.plot(timeAxis, signalAxis)
    # plt.xlabel('Time Axis')
    # plt.ylabel('Amplitude')
    # # plt.xlim([-0.2,0.2])
    # plt.ylim([0,0.1])
    plt.subplot(2,1,1)
    plt.plot()
    plt.plot(timeAxis, signalAxis)
    plt.xlabel('Time Axis')
    plt.ylabel('Amplitude')
    # plt.xlim([0,2*10^-8])
    plt.ylim([-0.1,0.1])
    plt.subplot(2,1,2)
    plt.plot()
    plt.plot(timeAxis, absSignal)
    plt.xlabel('Time Axis')
    plt.ylabel('Absolute Amplitude')
    # plt.xlim([0,2*10^-8])
    plt.ylim([0,0.1])
    plt.draw()
    plt.pause(0.0000000001)

def processRawSignal():
    rospy.init_node('processRawSignal', anonymous=True)
    rospy.Subscriber("rawSignal", rawSignal, callback)
    plt.ion()
    plt.show()
    rospy.spin()
        
if __name__ == '__main__':
    processRawSignal()