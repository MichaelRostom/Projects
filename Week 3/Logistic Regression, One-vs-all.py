from scipy.io import loadmat  # For loading the mat file
import numpy as np
from scipy import optimize as opt

# Load the date from the mat file
Loaded_Data = loadmat('ex3data1.mat')
X = Loaded_Data['X']
y_all = Loaded_Data['y']
for i in range(5000) :
    if y_all[i] == 10 :
        y_all[i] = 0

# Set some  initial values
input_layer_size = 400  # 20x20 Input Images of Digits
num_labels = 10  # 10 labels, from 1 to 10
# (note that we have mapped "0" to label 10)
m, n = X.shape
X = np.hstack((np.ones((m, 1)), X))
lambda_ = 0.1


# Calculate the sigmoid function
def sigmoid(z) :
    return 1 / (1 + np.exp(-z))


# Calculate the Cost Function and the gradient
def costFunction(theta, X, y) :
    theta = theta.reshape(-1, 1)
    hx = sigmoid(X @ theta)
    Jbefore = (-1 / m) * (y.transpose() @ np.log(hx) + (1 - y).transpose() @ np.log(1 - hx))
    J = Jbefore + (lambda_ / (2 * m)) * (np.sum(theta ** 2) - theta[0] ** 2)
    return J


def Grad(theta, X, y) :
    theta = theta.reshape(-1, 1)
    hx = sigmoid(X @ theta)
    gefore = (1 / m) * (X.transpose() @ (hx - y))
    g = gefore + (lambda_ / m) * theta
    g[0] = gefore[0]
    return g


initial_theta = np.zeros((n + 1, 1))
all_theta = np.zeros((num_labels, n + 1))

# Train multiple classifiers
for current in range(num_labels) :
    y = (y_all == current).astype(int)
    Result = opt.minimize(fun=costFunction,
                          x0=initial_theta,
                          args=(X, y),
                          method='TNC',
                          jac=Grad, options={'disp' : False, 'maxiter' : 1000})
    print(costFunction(Result.x, X, y), current)
    theta = Result.x
    theta = theta.reshape(-1, 1)
    all_theta[current, :] = theta.transpose()

# Use the new theta to predict values and calculate the percentage
hx = sigmoid(all_theta @ X.transpose())
p = np.argmax(hx, axis=0)  # Return the index of max values
p = p.reshape(-1, 1)
temp = p == y_all
percentage = np.mean(temp) * 100
print(str(percentage) + '%')
