import numpy as np

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

# Cost function
'''def Calc_Cost(X,Y,theta):
    squared_err = (np.subtract(np.matmul(X, theta), Y)) ** 2
    return 1 / (2 * m) * squared_err.sum()

print(Calc_Cost(X,y,theta))'''
# add the alpha value
theta = np.zeros((3, 1))
alpha = 0.01
iterations = 800

# run gradient descent
Delta = np.ones((X.shape[1], 1))  #
for iter in range(iterations) :
    op = np.subtract(np.matmul(X, theta), y)
    op = op.transpose()
    for j in range(X.shape[1]) :
        Delta[j, 0] = 1 / m * np.matmul(op, X[:, j].reshape((m, 1)))
    theta = np.subtract(theta, alpha * Delta)

print(theta)

# normal equations
X_data = np.hstack([Ones, X_data])
theta1 = np.matmul(X_data.transpose(), X_data)
theta1 = np.linalg.inv(theta1)
theta1 = np.matmul(theta1,np.matmul(X_data.transpose(),y))
print(theta1)
