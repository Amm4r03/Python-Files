import numpy as np

# Define the function and its gradient
def f(x):
    A = np.array([[2, 1], [1, 20]])
    b = np.array([[5], [3]])
    return 0.5 * np.dot(np.dot(x.T, A), x) - np.dot(b.T, x)

def gradient_f(x):
    return np.array([x[0] + 0.5 * x[1] - 5, 0.5 * x[0] + 20 * x[1] - 3])

# Gradient descent algorithm
def gradient_descent(x_init, learning_rate, num_iterations):
    x = x_init
    for i in range(num_iterations):
        gradient = gradient_f(x)
        x = x - learning_rate * gradient
    return x

# Initial point
x_init = np.array([[-3], [-1]])

# Learning rate and number of iterations
learning_rate = 0.01
num_iterations = 1000

# Perform gradient descent
x_opt = gradient_descent(x_init, learning_rate, num_iterations)

print("Optimal solution:")
print(x_opt)
print("Optimal function value:")
print(f(x_opt))