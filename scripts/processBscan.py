#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

y = []
z = []
dist = 0
i= 0

def callback(data):
    global y,z,i
    # convert amplitude value into array for computing
    raw = data.amplitude
    rawAmp = raw[0:2000]
    # updating list for plotting
    y.append(xdistance()) 
    z.append(rawAmp)

    # inverting amplitude value to get a vertical plot
    z = zip(*z)
    y_min, y_max = np.asarray(z).min(), np.asarray(z).max()
    # Plotting raw signal
    plt.ylim(2000,0)
    plt.xlim(0,50)
    plt.pcolormesh(z,cmap = 'gist_gray',vmin=y_min, vmax=y_max, xticklabels = y)
    plt.title('Raw Signal')
    plt.autoscale(enable=True,axis='both',tight=True)
    plt.draw()
    plt.pause(0.0000001)
    plt.show()
    y = zip(*y)
    i = i + 1

def xdistance():
    global dist
    dist = dist + 1
    return dist
        
if __name__ == '__main__':
    rospy.init_node('livePlot', anonymous=True)
    plt.ion()
    rawSignal = rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()