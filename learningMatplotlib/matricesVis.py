import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define two basis vectors
v1 = np.array([1, 0, 2])  # Adjust the z-component of v1
v2 = np.array([0, 1, 1])  # Adjust the z-component of v2

# Create a grid of points in the plane spanned by the basis vectors
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x, y)
Z = v1[2]*X + v2[2]*Y  # Equation of the plane: z = v1[2]*x + v2[2]*y

# Plot the 3D plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5)

# Plot basis vectors
origin = [0, 0, 0]
ax.quiver(*origin, *v1, color='r')
ax.quiver(*origin, *v2, color='g')

# Set labels and show plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('Span of two basis vectors')
plt.show()
