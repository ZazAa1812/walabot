#!/usr/bin/env python
import rospy
from walabot.msg import signal
import matplotlib.pyplot as plt
import numpy as np

processed_data = []
j = 0
def callback(data):
    global processed_data,j
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
    plt.ylim([-0.06,0.06])
    # Plotting absolute Ascan (without noise)
    plt.subplot(2,1,2)
    plt.plot()
    plt.plot(timeAxis, absSignal)
    plt.title('Absolute Ascan Graph')
    plt.xlabel('Time Axis')
    plt.ylabel('Absolute Amplitude')
    plt.ylim([0,0.06])
    plt.subplots_adjust(hspace=0.5)
    plt.draw()
    plt.pause(0.01)
    j = j + 0.02

    # Experiment 1#
#     if j==40:
#         ishut = "shutdown"
#         plt.savefig('src/walabot/data/depthcalibration/fiveAnt/BC5PairObject.png',bbpx_inches='tight')
#         rospy.signal_shutdown(ishut)

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