#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt

dist = 0
plt.style.use('ggplot')
line1 = []
x = []
y = []

def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        # plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1

def callback(data):
    global line1,x,y
    raw = np.asarray(data.amplitude)
    temp = abs(raw)
    amp = temp.tolist()
    temp = xdistance()
    x.append(temp)
    y.append(amp)
    print x
    print len(y)
    line1 = live_plotter(x,y,line1)

def xdistance():
    global dist
    dist = dist + 1
    return dist
        
if __name__ == '__main__':
    rospy.init_node('livePlot', anonymous=True)
    rawSignal = rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()