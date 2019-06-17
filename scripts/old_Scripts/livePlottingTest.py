#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

dist = 0
x = []
y = []
z = []
a = 0

def callback(data):
    global x,y,z,a
    raw = np.asarray(data.amplitude)
    temp = abs(raw)
    amp = temp.tolist()
    tempDist = xdistance()
    x.append(tempDist)
    y.append(amp)
    z.append(amp)
    z = zip(*z)
    print(len(y))
    print(len(y[0]))

    # Plotting
    plt.ion()
    plt.clf()
    plt.plot()
    plt.pcolor(z,cmap = 'gist_gray')
    plt.title('default')
    plt.tight_layout()
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