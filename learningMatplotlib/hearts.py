from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np

def graphValues(x, a):
    y = x ** 2/3 + 0.9 * (12.5 - x ** 2) ** (0.5) * sin(a * pi * x)
    return y

a = 9

xPlot = np.arange(-3.4, 3.41, 0.005)

yPlot = []

# print(xPlot, yPlot)

for i in xPlot:
    yPlot.append(graphValues(i, a))

plt.plot(xPlot, yPlot)
plt.axis('equal')
plt.title("testing")

plt.show()