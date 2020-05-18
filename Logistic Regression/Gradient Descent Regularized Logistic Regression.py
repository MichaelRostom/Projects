import numpy as np
from matplotlib import pyplot as plt

# Load the Data into X and y
Data = np.genfromtxt('ex2data2.txt', delimiter=',')
X = Data[:, 0 :2]
y = Data[:, 2]

# Plot the data
def plotData(X, y):
    # Create New Figure
    fig = plt.figure()

   
    X_Ad = X[np.where(y > 0)[0], :]  # Get only the admitted students
    X_NAd = X[np.where(y < 1)[0], :]  # Get only the NOT admitted students
    plt.scatter(X_Ad[:, 0], X_Ad[:, 1], marker='+', color='k',
                label='Admitted Students', s=100 )  # plots the admitted students
    plt.scatter(X_NAd[:, 0], X_NAd[:, 1], marker='o', color='y',
                label='Not Admitted Students', s=100)  # plots the NOT admitted students
   


# Map the X features
def mapFeature(X1, X2, degree=6) :
    if X1.ndim > 0 :
        out = [np.ones(X1.shape[0])]
    else :
        out = [np.ones(1)]

    for i in range(1, degree + 1) :
        for j in range(i + 1) :
            out.append((X1 ** (i - j)) * (X2 ** j))

    if X1.ndim > 0 :
        return np.stack(out, axis=1)
    else :
        return np.array(out)
X = mapFeature(X[:, 0], X[:, 1])

# set some important values
m, n = X.shape
y = y.reshape((m, 1))
lambda_ = 1
theta = np.zeros((n, 1))
alpha =0.03
iterations = 30000


# calculate the sigmoid function
def sigmoid(x) :
    return 1 / (1 + np.exp(-x))



# Calculate the cost function
def costFunction(X, y, theta) : 
    hx = sigmoid(X @ theta)
    Jbefore = (-1 / m) *(y.transpose() @ np.log(hx) + (1 - y).transpose() @ np.log(1 - hx))
    J = Jbefore + (lambda_/( 2 * m))*(np.sum(theta**2) - theta[0]**2)     
    return J



# run gradient descent
J_history = [] # For plotting the cost function over iterations
numbers = [] # For plotting the cost function over iterations
for i in range(iterations) :
    hx = sigmoid(X @ theta)
    theta = theta - alpha * ((1 / m) * (X.transpose() @ (hx - y))+(lambda_/m)*(theta))
    temp = X.transpose() @ (hx - y)
    theta[0] = theta[0] - alpha *(1/m)*temp[0]
    costfunc = costFunction(X, y, theta)
    print(costfunc,i)
    numbers.append(i)
    J_history.append(costfunc[0])

# Plot the cost function over iterations
plt.plot(numbers, J_history)
plt.xlabel('iterations')
plt.ylabel('Cost')
plt.title('Cost per iteration')
plt.show()


# PLot the decision boundary
def plotDecisionBoundary(plotData, theta, X, y):
    # make sure theta is a numpy array
    theta = np.array(theta)

    # Plot Data (remember first column in X is the intercept)
    plotData(X[:, 1:3], y)

    if X.shape[1] <= 3:
        # Only need 2 points to define a line, so choose two endpoints
        plot_x = np.array([np.min(X[:, 1]) - 2, np.max(X[:, 1]) + 2])

        # Calculate the decision boundary line
        plot_y = (-1. / theta[2]) * (theta[1] * plot_x + theta[0])

        # Plot, and adjust axes for better viewing
        plt.plot(plot_x, plot_y)

        # Legend, specific for the exercise
        plt.legend(['Admitted', 'Not admitted', 'Decision Boundary'])
        plt.xlim([30, 100])
        plt.ylim([30, 100])
    else:
        # Here is the grid range
        u = np.linspace(-1, 1.5, 50)
        v = np.linspace(-1, 1.5, 50)

        z = np.zeros((u.size, v.size))
        # Evaluate z = theta*x over the grid
        for i, ui in enumerate(u):
            for j, vj in enumerate(v):
                z[i, j] = np.dot(mapFeature(ui, vj), theta)

        z = z.T  # important to transpose z before calling contour
        # print(z)

        # Plot z = 0
        plt.contour(u, v, z, levels=[0], linewidths=2, colors='g')
        plt.contourf(u, v, z, levels=[np.min(z), 0, np.max(z)], cmap='Greens', alpha=0.4)

plotDecisionBoundary(plotData, theta, X, y)
plt.show()