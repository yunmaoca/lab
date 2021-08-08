#
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xlabel.html
#
#
#https://matplotlib.org/stable/tutorials/introductory/sample_plots.html
#https://www.w3schools.com/python/matplotlib_bars.asp


#Ohlone CNET-142 Python class Example
#7/18/21
#
#
#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


import csv

Axlist = [] # list for x-coordinates
Aylist = []

"""

Read excel csv file and load it to x,y coordinate list (Axlist, Aylist)


"""

with open('COVID_CA.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        Axlist.append(row[0])  # add to the list
        Aylist.append(int(row[2]))

# plot the graph based on Axlist and Aylist
#
# plt.plot(Axlist,Aylist, label='CA')
plt.bar(Axlist,Aylist, label='CA')

#plt.plot(Axlist,Aylist, label='CA')


ax = plt.gca()   # get current axes
monthFrequency = mdates.MonthLocator(interval=1)
ax.xaxis.set_major_locator(monthFrequency)   # label for x-axis

plt.xticks(rotation=90, fontsize=6)   # rotate the label 90 degree
# only print out every other x label so it will fit
# If remove the for loop, labels will overlap eacher other
"""
for label in ax.get_xaxis().get_ticklabels()[::1]:
    label.set_visible(False)
    
"""

#Add labels to line plots (annotation)
# zip joins x and y coordinates in pairs
#
def annatationLabel(xlist, ylist):
    count = 0  #used to only plot out annatation for every other number
    for x,y in zip(xlist,ylist):
        # for odd number: count %2 > 0; or use count to control
        # when to put annatation so it doesn't overlap
        if (count == 20):   # print out every x number, you can
    #     if (count %2) > 0: # this is odd number
#           label = "{:.2f}".format(y)
            label = (int)(y)
            plt.annotate(label,   # this is the text
                         (x,y),   # this is the point to label
                         textcoords="offset points",  # how to position
                         xytext=(0,10),    # distance from text to points
                         rotation=90,
                         fontsize=8,
                         ha='center')   # horitzontal alignment can be less
            count = 0
        else:
            count = count + 1

def covidChart():
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('# of Cases')
    plt.title('CA COVID Stats')
    annatationLabel(Axlist, Aylist)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    covidChart()


  
    
