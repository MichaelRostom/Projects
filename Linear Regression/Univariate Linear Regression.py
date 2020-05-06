import numpy as np
import matplotlib.pyplot as plt

X, Y = np.loadtxt('ex1data1.txt', delimiter=',', unpack=True)
m = Y.shape[0]  # Sets the length
X = X.reshape((m, 1))  # reshapes into 2 dimensions
Y = Y.reshape((m, 1))  # reshapes into 2 dimensions
X = np.hstack([np.ones((m, 1)), X]) # adds the ones to the X
plt.scatter(X[:, 1], Y, label='Training Data', marker='x', color='r')  # plots the data
plt.title('Figure 1')   # plots the data
plt.xlabel('Population of City in 10,000s') # plots the data
plt.ylabel('Profit in $10,000s')    # plots the data
plt.show()

theta = np.zeros((2, 1))  # Parameters
# settings
alpha = 0.01
itertions = 1500


# cost function
def Cost_Function(X, Y, theta) :
    squared_err = (np.subtract(X@ theta, Y)) ** 2  #
    return 1 / (2 * m) * squared_err.sum()


# Gradient Descent
for iter in range(itertions) :
    Delta = 1 / m * X.transpose() @ np.subtract(X@ theta, Y)
    theta = np.subtract(theta, alpha * Delta)
plt.scatter(X[:, 1], Y, label='Training Data', marker='x', color='r')  # plots the data
plt.title('Figure 1')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
x = np.linspace(5, 23, 100)
y = theta[0, 0] + theta[1, 0] * x
plt.plot(x, y, '-r', label='Linear regression', color='blue')
plt.legend()
plt.show()
