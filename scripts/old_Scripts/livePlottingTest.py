#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

dist = 0
x = []
y = []
z = []

def callback(data):
    global line1,x,y,z
  
    raw = np.asarray(data.amplitude)
    temp = abs(raw)
    amp = temp.tolist()
    tempDist = xdistance()
    x.append(tempDist)
    y.append(amp)
    z.append(amp)
    z = np.asarray(z)
    print(len(y))
    print(len(y[0]))
    a = np.random.rand(1,6)

    # Plotting
    plt.ion()
    plt.clf()
    plt.plot()
    plt.pcolor(z)
    plt.title('default')
    plt.tight_layout()
    z = z.tolist()
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