#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
z = []
a = 0

def callback(data):
    global x,y,z,a
    # convert amplitude value into array for computing
    rawAmp = data.amplitude
    rawAmpArr = np.asarray(rawAmp)
    # get absolute value for second plot and turn back to list
    absRaw = abs(rawAmpArr)
    absAmp = absRaw.tolist()
    tempDist = xdistance()
    # updating list for plotting
    x.append(tempDist)
    y.append(rawAmp)
    z.append(absAmp)
    # inverting amplitude value to get a vertical plot
    y = zip(*y)
    z = zip(*z) 
    # to set colormap intensity limit
    y_min, y_max = min(np.asarray(y)), max(np.asarray(y)) 
    z_min, z_max = min(np.asarray(z)), max(np.asarray(z)) 

    # Plotting
    # Raw signal
    plt.ion()
    plt.clf()
    # Figure for comparing raw signal and absolute signal intensity
    plt.figure(1)
    plt.subplot(1,2,1)
    plt.plot()
    plt.ylim(3000,0)
    plt.pcolor(y,cmap = 'gist_gray',vmin=y_min, vmax=y_max)
    plt.title('Raw Signal')
    plt.subplot(1,2,2)
    plt.plot()
    plt.ylim(3000,0)
    plt.pcolor(z,cmap = 'gist_gray',vmin=z_min, vmax=z_max)
    plt.title('Absolute Signal')
    plt.tight_layout()

    y = []
    z = []
    plt.pause(0.5)
    plt.show()

def xdistance():
    global dist
    dist = dist + 1
    return dist
        
if __name__ == '__main__':
    rospy.init_node('livePlot', anonymous=True)
    rawSignal = rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()