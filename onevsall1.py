#https://utkuufuk.github.io/2018/06/03/one-vs-all-classification/
import numpy as np
import scipy.io as sio
import scipy.optimize as opt

data = sio.loadmat("digits.mat")
x = data['X']  # the feature matrix is labeled with 'X' inside the file
# the target variable vector is labeled with 'y' inside the file
y = np.squeeze(data['y'])
np.place(y, y == 10, 0)  # replace the label 10 with 0
numExamples = x.shape[0]  # 5000 examples
numFeatures = x.shape[1]  # 400 features
numLabels = 10  # digits from 0 to 9


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost(theta, X, y):
    predictions = sigmoid(X @ theta)
    predictions[predictions == 1] = 0.999  # log(1)=0 causes error in division
    error = -y * np.log(predictions) - (1 - y) * np.log(1 - predictions)
    return sum(error) / len(y)


def cost_gradient(theta, X, y):
    predictions = sigmoid(X @ theta)
    return X.transpose() @ (predictions - y) / len(y)


X = np.ones(shape=(x.shape[0], x.shape[1] + 1))
X[:, 1:] = x
classifiers = np.zeros(shape=(numLabels, numFeatures + 1))

for c in range(0, numLabels):
    label = (y == c).astype(int)
    initial_theta = np.zeros(X.shape[1])
    classifiers[c, :] = opt.fmin_cg(cost, initial_theta, cost_gradient, (X, label), disp=0)
classProbabilities = sigmoid(X @ classifiers.transpose())
predictions = classProbabilities.argmax(axis=1)
print("Training accuracy:", str(100 * np.mean(predictions == y)) + "%")
