#!/usr/bin/env python
import rospy
from walabot.msg import signal
import matplotlib.pyplot as plt
import numpy as np

processed_data = []

def callback(data):
    global processed_data
    signalAxis = data.amplitude
    timeAxis = data.time
    # print(type(signalAxis))
    temp = abs(np.asarray(signalAxis))
    absSignal = temp.tolist()
    # Current data being processed and will be publish
    processed_data = absSignal
    plt.clf()
    # Plotting Ascan (without noise)
    plt.subplot(2,1,1)
    plt.plot()
    plt.plot(timeAxis, signalAxis)
    plt.title('Ascan Graph')
    plt.xlabel('Time Axis')
    plt.ylabel('Amplitude')
    # plt.ylim([-0.05,0.05])
    # Plotting absolute Ascan
    plt.subplot(2,1,2)
    plt.plot()
    plt.plot(timeAxis, absSignal)
    plt.title('Absolute Ascan Graph')
    plt.xlabel('Time Axis')
    plt.ylabel('Absolute Amplitude')
    # plt.ylim([0,0.05])
    plt.subplots_adjust(hspace=0.5)
    plt.draw()
    plt.pause(0.01)

def processAscan():
    rospy.init_node('processAscan', anonymous=True)
    rospy.Subscriber("rawSignal", signal, callback)
    plt.ion()
    plt.show()
    rospy.spin()
        
if __name__ == '__main__':
    print('Running')
    processAscan()
    plt.ioff()