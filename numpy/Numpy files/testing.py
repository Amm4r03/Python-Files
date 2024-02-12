import numpy as np

A = np.array([[1, 2], [2, 1]])
U, S, V = np.linalg.svd(A)

print("{}, {}, {}".format(U, S, V))