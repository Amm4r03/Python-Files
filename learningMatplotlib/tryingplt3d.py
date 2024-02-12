import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import sqrt, pi, exp

# Define function for calculating PDF using formula
def standardNormalDist(x, sd, mean):
    e = 2.718
    return (1 / (sd * sqrt(2 * pi))) * exp(-0.5 * ((x - mean) / sd)**2)

# Generate data for a 3D surface plot of SND
mean = 0
sd = 1
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.vectorize(standardNormalDist)(X, sd, mean) * np.vectorize(standardNormalDist)(Y, sd, mean)

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability Density')
ax.set_title('3D Standard Normal Distribution')

plt.show()
