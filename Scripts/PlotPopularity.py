

from matplotlib.ticker import PercentFormatter

import pylab as plt
import numpy as np


x = list()
with open("../Results Stats 714/Nodes Community Membership & Outlier Score/membership&Score-1.csv", 'r') as readfile:
    for line in readfile:
        try:
            if int(line.split()[2].strip(',') ) == 1:
                x.append(float(line.split()[4]))
        except:
            pass

print(x)
xrounded = [ round(elem, 1) for elem in x ]
print(xrounded)

plt.title("Outlier Score of nodes participating in one community")
plt.hist(xrounded, bins=[0, 0.25, 0.5, 0.75, 1])
plt.show()

'''
x = list()
with open("../Draft Results COTILES/Nodes Community Membership & Outlier Score/membership&Score-3.csv", 'r') as readfile:
    for line in readfile:
        try:
            if int(line.split()[2].strip(',') ) == 0:
                x.append(float(line.split()[4]))
        except:
            pass

print(x)
xrounded = [ round(elem, 1) for elem in x ]
print(xrounded)

plt.title("Outlier Score of nodes not participating in communities")
plt.hist(xrounded, bins=[0, 0.25, 0.5, 0.75, 1])
plt.show()
'''