import numpy as np
from matplotlib import pyplot as plt

# Load the data
Data = np.genfromtxt('ex1data2.txt', delimiter=',')

# assign the variables
X_data = Data[:, 0 :2]
y = Data[:, 2]
y = y.reshape((47, 1))
m = y.shape[0]

# Feature Normalization
mu = np.mean(X_data, axis=0)
sigma = np.std(X_data, axis=0, ddof=1)
X_norm = (X_data - mu) / sigma

# add the ones to X
Ones = np.ones((m, 1))
X = np.hstack([Ones, X_norm])

# add the alpha value
theta = np.zeros((3, 1))
alpha = 0.01
iterations = 800

def Cost_Function(X, Y, theta) :
    squared_err = (np.subtract(X@ theta, Y)) ** 2  #
    return 1 / (2 * m) * squared_err.sum()

# run gradient descent
J_history = [] # For plotting the cost function over iterations
numbers = [] # For plotting the cost function over iterat
for iter in range(iterations) :
    Delta = 1 / m * (X.transpose() @ np.subtract(X @ theta, y))
    theta = np.subtract(theta, alpha * Delta)
    costfunc = Cost_Function(X, y, theta)
    print(costfunc, iter)
    numbers.append(iter)
    J_history.append(costfunc)
# Plot the cost function over iterations
plt.plot(numbers, J_history)
plt.xlabel('iterations')
plt.ylabel('Cost')
plt.title('Cost per iteration')
plt.tight_layout()
plt.show()

# normal equations
X_data = np.hstack([Ones, X_data])
theta1 = X_data.transpose() @ X_data
theta1 = np.linalg.inv(theta1)
theta1 = theta1 @ np.matmul(X_data.transpose(), y)
print(theta1)
