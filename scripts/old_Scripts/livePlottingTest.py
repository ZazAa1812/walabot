#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

dist = 0
x = []
y = []
zsa = []

def callback(data):
    global line1,x,y,zsa

    raw = np.asarray(data.amplitude)
    temp = abs(raw)
    amp = temp.tolist()
    tempDist = xdistance()
    x.append(tempDist)
    y.append(amp)
    a = np.random.rand(1,6)
    print a
    # zsa.append(a)
    # Plotting
    plt.ion()
    plt.clf()
    plt.plot()
    plt.pcolor(a)
    plt.title('default')
    plt.tight_layout()
    plt.pause(0.5)
    plt.show()

    print zsa
    print x
    print len(y)

def xdistance():
    global dist
    dist = dist + 1
    return dist
        
if __name__ == '__main__':
    rospy.init_node('livePlot', anonymous=True)
    rawSignal = rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()