#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt
from walabot.msg import distanceTravelled
import message_filters

y = []
z = []
dist = []
# i= 0

def callback(rawSignaldata, distanceTravelleddata):
    global y,z,dist
    # convert amplitude value into array for computing
    raw = rawSignaldata.amplitude
    dist = distanceTravelleddata.distance
    print dist
    rawAmp = raw[0:2000]
    # updating list for plotting
    # y.append(xdistance()) 
    z.append(rawAmp)

    # inverting amplitude value to get a vertical plot
    z = zip(*z)
    y_min, y_max = np.asarray(z).min(), np.asarray(z).max()
    # Plotting raw signal
    plt.ylim(2000,0)
    plt.xlim(0,50)
    plt.pcolormesh(z,cmap = 'gist_gray',vmin=y_min, vmax=y_max) #xticklabels = y)
    plt.title('Raw Signal')
    plt.autoscale(enable=True,axis='both',tight=True)
    plt.draw()
    plt.pause(0.0000001)
    plt.show()
    y = zip(*y)

# def xdistance():
#     global dist
#     dist = dist + 1
#     return dist
        
if __name__ == '__main__':
    rospy.init_node('processBscan', anonymous=True)
    plt.ion()
    rawSignaldata = message_filters.Subscriber("rawSignal", signal)
    distanceTurtleTravdata = message_filters.Subscriber('distanceTravelled',distanceTravelled)
    ts = message_filters.ApproximateTimeSynchronizer([rawSignaldata, distanceTurtleTravdata],10,0.1)
    ts.registerCallback(callback)
    rospy.spin()