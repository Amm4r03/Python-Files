# performs matrix inversion
import numpy as np

a = np.array([[25, 1, 2], [1, 30, 3], [5, 1, 35]])

b = np.linalg.inv(a)

print(f"original matrix : \n{a}")

print(f"inverted matrix : \n{b}")