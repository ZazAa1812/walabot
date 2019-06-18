#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

t = []
y = []

def callback(data):
    global t,y
    # convert amplitude value into array for computing
    rawAmp = data.amplitude
    test = [1,2,3]
    # updating list for plotting
    t.append(test)
    y.append(rawAmp)
    # inverting amplitude value to get a vertical plot
    t = zip(*t)
    y = zip(*y)
    print t
    print len(y)
    # Plotting raw signal
    plt.ion()
    plt.plot()
    plt.ylim(3000,0)
    plt.pcolor(y,cmap = 'gist_gray')#,vmin=y_min, vmax=y_max)
    plt.title('Raw Signal')
    plt.pause(0.5)
    plt.show()
    t = zip(*t)
    y = zip(*y)

def xdistance():
    global dist
    dist = dist + 1
    return dist
        
if __name__ == '__main__':
    rospy.init_node('livePlot', anonymous=True)
    rawSignal = rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()