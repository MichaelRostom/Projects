import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize as opt

# Load Data
Loaded_Data = np.genfromtxt('eX2data1.txt', delimiter=',')  # Get Data from file
X = Loaded_Data[:, 0 :2]  # Load X
y = Loaded_Data[:, 2]  # load y
m = y.shape[0]  # Set The Number OF training examples
n = X.shape[1]  # Sets The Number of features
y = y.reshape((m, 1))  # reshape y into correct shape

# Plot the Data
X_Ad = X[np.where(y > 0)[0], :]  # Get only the admitted students
X_NAd = X[np.where(y < 1)[0], :]  # Get only the NOT admitted students
plt.scatter(X_Ad[:, 0], X_Ad[:, 1], marker='+', color='k',
            label='Admitted Students', s=100 )  # plots the admitted students
plt.scatter(X_NAd[:, 0], X_NAd[:, 1], marker='o', color='y',
            label='Not Admitted Students', s=100)  # plots the NOT admitted students
plt.xlabel('EXam 1 score')
plt.ylabel('EXam 2 score')
plt.legend()
plt.show()
X_Ad = X[np.where(y > 0)[0], :]  # Get only the admitted students
X_NAd = X[np.where(y < 1)[0], :]  # Get only the NOT admitted students
plt.scatter(X_Ad[:, 0], X_Ad[:, 1], marker='+', color='k',
            label='Admitted Students', )  # plots the admitted students
plt.scatter(X_NAd[:, 0], X_NAd[:, 1], marker='o', color='y',
            label='Not Admitted Students')  # plots the NOT admitted students
plt.xlabel('EXam 1 score')
plt.ylabel('EXam 2 score')
plt.legend()


# Calculate the sigmoid function
def sigmoid(z) :
    g = np.zeros(z.shape)
    g = 1 / (1 + (np.exp(-z)))
    return g


# add the intercept form to X
X = np.hstack([np.ones((m, 1)), X])

# Initialize theta
theta = np.zeros((n + 1, 1))


# Calculate the cost function
def gradient(theta, X, y) :
    theta = theta.reshape(-1, 1)
    hx = sigmoid(X @ theta)
    grad = (1 / m) * (np.transpose(X) @ (hx - y))
    return grad


def costFunction(theta, X, y) :
    theta = theta.reshape(-1, 1)
    hx = sigmoid(X @ theta)
    j1 = np.transpose(np.log(hx)) @ y
    j2 = (np.transpose(np.log(1 - hx))) @ (1 - y)
    J = (-1 / m) * (j1 + j2)
    return J


# Compute and display initial cost and gradient
initial_theta = np.zeros((n + 1, 1))
cost= costFunction(initial_theta,X,y)
grad = gradient(initial_theta,X,y)

print('Cost at initial theta (zeros): \n', cost)
print('Expected cost (approx): 0.693\n')
print('Gradient at initial theta (zeros): \n')
print(' \n', grad)
print('Expected gradients (approx):\n -0.1000\n -12.0092\n -11.2628\n')

# Compute and display cost and gradient with non-zero theta
test_theta = np.array(([-24], [0.2], [0.2]))
cost= costFunction(test_theta,X,y)
grad = gradient(test_theta,X,y)
print(cost)
print('\nCost at test theta: %f\n', cost)
print('Expected cost (approx): 0.218\n')
print('Gradient at test theta: \n')
print(' %f \n', grad)
print('Expected gradients (approx):\n 0.043\n 2.566\n 2.647\n')

# Optimize theta using fminunc
# result = opt.fmin(costFunction, x0=theta, args=(X, y), maxiter=500, full_output=True)
Result = opt.minimize(fun = costFunction, 
                                 x0 = theta, 
                                 args = (X, y),
                                 method = 'TNC',
                                 jac = gradient, options={'gtol': 1e-3, 'disp': True, 'maxiter': 1000})
cost = costFunction(Result.x, X, y)
theta = Result.x

# Print theta to screen
print('Cost at theta found by fminunc: ', cost)
print('Expected cost (approx): 0.203\n')
print('theta: ', theta)
print('Expected theta (approx):')
print(' -25.161 0.206 0.201')

# PLot the decision boundary
plot_x = [min(X[:, 1]) - 2, max(X[:, 1]) + 2]
plot_y = [1, 1]
plot_y[0] = (-1 / theta[2]) * ((theta[1] * plot_x[0]) + theta[0])
plot_y[1] = (-1 / theta[2]) * ((theta[1] * plot_x[1]) + theta[0])
plt.plot(plot_x,plot_y)
plt.show()

# Predict new stuff
prob = sigmoid([1, 45, 85] @ theta)
print('For a student with scores 45 and 85, we predict an admission probability of \n', prob);
print('Expected value: 0.775 +/- 0.002\n\n')


# Compute Accuracy
def predict(theta, X) :
    p = (sigmoid(X @ theta)) >= 0.5
    return p


p = predict(theta, X)
per = np.ones((m, 1))
for i in range(m) :
    if p[i] == True and y[i] == 1 :
        per[i] = 1
    if p[i] == False and y[i] == 0 :
        per[i] = 1
    if p[i] == False and y[i] == 1 :
        per[i] = 0
    if p[i] == True and y[i] == 0 :
        per[i] = 0
mean = np.mean(per)*100
print('Train Accuracy: \n', mean)
print('Expected accuracy (approx): 89.0\n')
# def gradient(X, y, theta) :
#     hx = sigmoid(X @ theta)
#     jbefore = (-1 / m) * ((np.log(hx).transpose() @ y) + (np.log(1 - hx)).transpose() @ (1 - y))
#     J = jbefore + (lambda1 / (2 * m)) * (sum(theta ** 2) - theta.item(0) ** 2)
#     gbefore = (1 / m) * (X.transpose() @ (hx - y))
#     # print(gbefore.shape)
#     grad = gbefore + (lambda1 / m) * theta
#     grad[0] = gbefore[0]
#     return J, grad
#
#
# def costFunction(theta, X, y) :
#     return gradient(X, y, theta)[0]

