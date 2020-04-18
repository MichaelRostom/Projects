import numpy as np

Raw_Data = np.genfromtxt('ex1data1.txt', delimiter=',')  # loads the data from the file

m = Raw_Data.shape[0]  # Sets the length

Y = np.ones((m, 1))
Y[:, 0] = Raw_Data[:, 1]
X = np.ones((m, 2))
X[:, 1] = Raw_Data[:, 0]  # adds the column of ones to the x's

theta = np.zeros((2, 1))  # Parameters
# settings
alpha = 0.01
itertions = 1500


# cost function
def Cost_Function(X, Y, theta) :
    squared_err = (np.subtract(np.matmul(X, theta), Y)) ** 2  #
    return 1 / (2 * m) * squared_err.sum()


# Gradient Descent
for iter in range(itertions) :
    Delta = 1/m*np.matmul(X.transpose(),np.subtract(np.matmul(X, theta), Y))
    theta = np.subtract(theta, alpha * Delta)
print(theta)
