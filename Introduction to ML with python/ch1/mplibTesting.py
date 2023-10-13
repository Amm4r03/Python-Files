import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.plot(x, y, marker="x")
plt.savefig("sine_plot.png")

plt.show