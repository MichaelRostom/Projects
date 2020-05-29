import numpy as np
from scipy.io import loadmat  # For loading the mat file

# Load theta1, theta2, X, y from the mat file
Loaded_Parameters = loadmat('ex3weights.mat')
Loaded_Data = loadmat('ex3data1.mat')
theta1 = Loaded_Parameters['Theta1']  # 25x401
theta2 = Loaded_Parameters['Theta2']  # 10x26
X = Loaded_Data['X']
y_all = Loaded_Data['y']

# set some values, and add the intercept term to X
m, n = X.shape
X = np.hstack((np.ones((m, 1)), X))


# Calculate the sigmoid function
def sigmoid(z) :
    return 1 / (1 + np.exp(-z))


# Calculate the Feed Forward network
a2 = sigmoid(theta1 @ X.transpose())  # Calculate the second layer
a2 = np.vstack((np.ones((1, m)), a2))  # add the bias unit to the second layer

hx = sigmoid(theta2 @ a2)  # Calculate the third layer

# Use the Neural Network to predict new values
p = np.argmax(hx,
              axis=0) + 1  # get the index of max values of predictions, the plus one because this how it was trained
p = p.reshape(-1, 1)
temp = p == y_all
percentage = np.mean(temp) * 100
print(str(percentage) + '%')
