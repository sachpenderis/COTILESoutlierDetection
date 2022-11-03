

from matplotlib.ticker import PercentFormatter

import pylab as plt
import numpy as np



x = list()
with open("../ResultsUnix3030/Nodes Community Membership/membership-0.csv", 'r') as readfile:
    for line in readfile:
        x.append(int(line.split()[-1]))





plt.hist(x, bins='auto')
plt.show()