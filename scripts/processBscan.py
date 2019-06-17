#!/usr/bin/env python
import rospy
from walabot.msg import signal
import matplotlib.pyplot as plt
import numpy as np
import time
import math

###############Failed Depth Calculation Function###################
# the calculation was made using the value of the first peak amplitude from the signal
# equation v= (c/sqrt(dielectric constant))*10^-9
# depth = (tcurrent - tinitial)/(2*v)
###############End comment###################

# speed of light m/s
# c = 299792458
# dielectric_constant = 1

# def callback(data):
#     global c, dielectric_constant
#     amplitude = data.amplitude
#     timeAxis = data.time  
#     # rospy.loginfo(amplitude) 
#     strongAmplitude = max(amplitude)
#     print(strongAmplitude)
#     indexAmp = amplitude.index(strongAmplitude) 
#     tcurrent = timeAxis[indexAmp]
#     tinitial = timeAxis[0]
#     # travel_speed_pulse, v
#     v = (c/math.sqrt(dielectric_constant))*10**-9
#     print('ni v sia')
#     print(v)
#     print(tcurrent - tinitial)
#     depth = (tcurrent - tinitial)/(2*v)*1000
#     print(depth)

######## Generating radargram using colormesh #########
def callback(data):
    amplitude = data.amplitude
    timeAxis = data.time


def processBscan():
    rospy.init_node('processBscan', anonymous=True)
    rospy.Subscriber("rawSignal", signal, callback)
    rospy.spin()
        
if __name__ == '__main__':
    processBscan()