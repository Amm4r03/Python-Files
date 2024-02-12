# performs matrix multiplication
import numpy as np

a = np.arange(1, 10).reshape(3, 3)

b = np.arange(2, 20, 2).reshape(3, 3)

# perform multiplication using dot() function
c = np.dot(a, b)

print(c)