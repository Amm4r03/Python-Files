import matplotlib.pyplot as plt

coords = [[1, 2], [3, 4], [6, 250], [10, 40]]

xPts = [i[0] for i in coords]
yPts = [i[1] for i in coords]

print(xPts, yPts)

plt.plot(xPts, yPts)
plt.show()