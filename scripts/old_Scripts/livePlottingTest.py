#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

dist = 0
x = []
y = []

def callback(data):
    global line1,x,y

    raw = np.asarray(data.amplitude)
    temp = abs(raw)
    amp = temp.tolist()
    tempDist = xdistance()
    x.append(tempDist)
    y.append(amp)
    # Plotting
    plt.ion()
    plt.clf()
    plt.plot()
    plt.pcolor(y)
    plt.title('default')
    plt.tight_layout()
    plt.show()
    zsa = np.random.rand(6,2)
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