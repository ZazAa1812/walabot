#!/usr/bin/env python
import rospy
from walabot.msg import rawSignal
from walabot.msg import processData
import matplotlib.pyplot as plt
import numpy as np

processed_data = []
pub = rospy.Publisher('processedAbsAscanData',processData,queue_size = 1000)
start_flag = False

def callback(data):
    global start_flag, processed_data
    signalAxis = data.amplitude
    timeAxis = data.time
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
    plt.ylim([-0.1,0.1])
    # Plotting absolute Ascan
    plt.subplot(2,1,2)
    plt.plot()
    plt.plot(timeAxis, absSignal)
    plt.title('Absolute Ascan Graph')
    plt.xlabel('Time Axis')
    plt.ylabel('Absolute Amplitude')
    plt.ylim([0,0.1])
    plt.subplots_adjust(hspace=0.5)
    plt.draw()
    plt.pause(0.01)
    if(not start_flag):
        start_flag = True

def pub_callback():
    global start_flag, pub, processed_data
    if(start_flag):
        pub.publish(processed_data)
        print("Processed data published")

def processAscan():
    rospy.init_node('processAscan', anonymous=True)
    while not rospy.is_shutdown():
        rospy.Subscriber("rawSignal", rawSignal, callback)
        # Will ensure processed data being published every 0.5 sec
        pub_callback()
        plt.ion()
        plt.show()
        rospy.sleep(1)
        
if __name__ == '__main__':
    print('Running')
    processAscan()