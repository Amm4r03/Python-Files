# trying to plot standard normal distribution curve using matplotlib
from math import sqrt, pi, exp
import matplotlib.pyplot as plt
import numpy as np

# define function for calculating PDF using formula
def standardNormalDist(x, sd, mean):
    e = 2.718
    return (1 / (sd * sqrt(2 * pi))) * exp(-0.5 * ((x - mean) / sd)**2)


# create vars
ans = []
mean = 100
sd = 15

# prints the curve upto 3.5 standard deviations from mean
gap = sd * 3.25
xplot = []

# removed this code with the code below to increase resolution in final graph
# for i in range(mean - gap, mean + gap + 1):
#     ans.append(standardNormalDist(i, sd, mean))
#     xplot.append(i)

# created list that has values from mean-gap to mean + gap with a smaller step value
# than what range function offers, thus increasing resolution in graph

# set value closer to 0 for greater resolution
resolution = 0.5

toCalc = np.arange(mean - gap, mean + gap + 1, resolution)
for val in toCalc:
    ans.append(standardNormalDist(val, sd, mean))

# plot the values
plt.plot(toCalc, ans)

# Draw vertical dotted lines for showing standard deviations
# first sd
plt.axvline(x=mean + sd, color='red', linestyle='dotted', label='first positive sd')
plt.axvline(x=mean - sd, color='red', linestyle='dotted', label='first negative sd')

# second sd
plt.axvline(x=mean + 2*sd, color='green', linestyle='dotted', label='second positive sd')
plt.axvline(x=mean - 2*sd, color='green', linestyle='dotted', label='second negative sd')

# third sd
plt.axvline(x=mean + 3*sd, color='orange', linestyle='dotted', label='third positive sd')
plt.axvline(x=mean - 3*sd, color='orange', linestyle='dotted', label='third negative sd')

plt.title("standard normal distribution", y = 1.05)
plt.suptitle(f"mean = {mean}, standard deviation = {sd}",y=0.915 , fontsize=8)
plt.xlabel("x")
plt.ylabel("probability density")

plt.show()