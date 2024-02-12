# performs matrix inversion
import numpy as np

a = np.array([[2, 3], [1, 2]])

b = np.linalg.inv(a)

print(b)