#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt
from walabot.msg import distanceTravelled
import message_filters
import xlwt
from xlwt import Workbook

y = []
z = []
dist = []
i = 0 # Counter for mock distance value
j=0
def callback(data):
    global y,z,dist,i,j
    # convert amplitude value into array for computing
    raw = data.amplitude
    rawAmp = raw[0:2000]
    # updating list for plotting
    z.append(rawAmp)
    dist.append(i)
    # print(dist)
    # inverting amplitude value to get a vertical B-scan plot
    z = zip(*z)
    y_min, y_max = np.asarray(z).min(), np.asarray(z).max()
    # Plotting raw signal
    if i==0:
        # Setting the figure onnce
        plt.figure(figsize=(15,8))

        # For experiment 2 #
        # wb = Workbook()
        # sheet1 = wb.add_sheet('Sheet 1')
        # sheet1.write(0,0, 'Timestamp')
        # sheet1.write(0,1, 'Distance')
    plt.clf()
    # Graph size is already made to suit the total distance travelled. If changed, edit here too.
    plt.ylim(2000,0)
    plt.xlim(0,30)
    plt.pcolormesh(z,cmap = 'gist_gray',vmin=y_min, vmax=y_max)
    plt.title('Bscan')
    plt.ylabel('Number of sample data')
    plt.xlabel('Distance Travelled')
    plt.xticks(np.arange(len(dist)),dist,rotation = 45)
    plt.draw() 
    plt.pause(0.0000001)
    plt.show()
    z = zip(*z)
    print (len(z))
    # Getting current time stamp
    tc = rospy.Time.now().to_sec()
    print tc

    # For experiment 2 #
    # sheet1.write(j,0,tc)
    # sheet1.write(j,1,i)
    # j = j +1

    # Mock distance value. Target distance = 0.6, hence 0.02 increments until it reaches 30 (0.02*30=0.6). 
    i = i + 0.02
    if len(z)==30:
        i = "shutdown"
        # Saving the graph image
        plt.savefig('src/walabot/data/dataBscan/WalabotBscan.png',bbox_inches='tight')
        rospy.signal_shutdown(i)
if __name__ == '__main__':
    rospy.init_node('processBscan', anonymous=True)
    plt.ion()
    # Delay to match with robot movement node
    rospy.sleep(1)
    rospy.Subscriber("rawSignal",signal,callback)
    rospy.spin()