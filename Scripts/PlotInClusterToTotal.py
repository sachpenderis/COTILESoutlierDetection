

from matplotlib.ticker import PercentFormatter

import pylab as plt
import numpy as np



x = list()

'''
with open("../Results Stats 1510/MaxIntegratedInClusterToTotalLabels.txt", 'r') as readfile:
    for line in readfile:
        x.append(float(line.split()[-1]))
'''

x= [1	,
1	,
1	,
0.2	,
0.22	,
1	,
0.5	,
1	,
0.17	,
1	,
0.43	,
1	,
1	,
0.8	,
0.43	,
1	,
0.89	,
0.5	,
0.4	,
1	,
0.5	,
1	,
0.5	,
0.57	,
1	,
0.44	,
1	,
1	,
1	,
1	,
1	,
0.5	,
1	,
0.36	,
0.43	,
1	,

]

plt.hist(x, bins='auto')
plt.title("Half Content Score of nodes participating in at least one community")
#plt.title("Proportion of node's links with a community to its total edges in the network")
#plt.title("Community focus of nodes belonging to at least one community")
plt.show()