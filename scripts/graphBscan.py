#!/usr/bin/env python
import rospy
from walabot.msg import dataBscan
import numpy as np
import matplotlib.pyplot as plt

y = []
z = []
dist = []

def callback(data):
    global y,z,dist
    # convert amplitude value into array for computing
    raw = data.amplitude
    rawAmp = raw[0:2000]
    # updating list for plotting 
    z.append(rawAmp)
    # inverting amplitude value to get a vertical plot
    z = zip(*z)
    y_min, y_max = np.asarray(z).min(), np.asarray(z).max()
    # Plotting raw signal
    plt.ylim(2000,0)
    plt.xlim(0,50)
    plt.pcolormesh(z,cmap = 'gist_gray',vmin=y_min, vmax=y_max) #xticklabels = y)
    plt.title('Bscan')
    plt.ylabel('Number of sample data')
    plt.xlabel('Mock distance travelled')
    plt.draw()
    plt.pause(0.0000001)
    plt.show()
    z = zip(*z)
        
if __name__ == '__main__':
    rospy.init_node('graphBscan', anonymous=True)
    plt.ion()
    rospy.Subscriber("processBscan",dataBscan,callback)
    rospy.spin()