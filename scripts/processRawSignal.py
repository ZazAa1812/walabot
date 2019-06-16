#!/usr/bin/env python
import rospy
from walabot.msg import rawSignal
import matplotlib.pyplot as plt

def callback(data):
    signalAxis = data.amplitude
    timeAxis = data.time
    rospy.loginfo(data.amplitude)
    plt.cla()
    plt.plot(timeAxis, signalAxis)
    plt.xlabel('Time Axis')
    plt.ylabel('Amplitude')
    # plt.xlim([-0.2,0.2])
    plt.ylim([-0.2,0.2])
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