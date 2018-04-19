#!Python3

#BioPhys 117 : February 13th 2018 : Summer Stern : Linear Fit

'''
The goal of this activity is to fit data to a line
'''

import matplotlib.pyplot as plt
import numpy as np

# parameters for fake data
slope=3
intercept=-5
noisemag=3

#now make the data
x = np.linspace(0, 10, 50); # this makes 50 points of evenly spaced points between 0 and 10
yexact = intercept+ x*slope #this makes the line
ywnoise = yexact+np.random.randn(np.size(x))*noisemag # this adds noise

plt.plot(x, yexact, 'r')
plt.scatter(x, ywnoise, c='b')

np.polyfit(x, ywnoise, 1)
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend(['data', 'fit'])
plt.show()
