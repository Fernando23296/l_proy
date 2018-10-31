#neural network for 9 entries and 1 binary answer
from matplotlib import pyplot as plt
import numpy as np

data = [[[282,   0],
        [209,  71],
        [216, 119],
        [187, 207],
        [297, 320],
        [267, 416],
        [229, 519],
        [242, 575],
        [281, 745],
        [282, 915],1],
        [[409,    0],
         [338,   66],
         [336,  132],
         [284,  264],
         [505,  330],
         [365,  462],
         [334,  528],
         [409,  594],
         [409,  726],
         [282, 915], 0]]


# activation function


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

# predict what the myster flower is!


# train

def train():
    #random init of weights
    w1 = np.random.randn()
    w2 = np.random.randn()
    w3 = np.random.randn()
    w4 = np.random.randn()
    w5 = np.random.randn()
    w6 = np.random.randn()
    w7 = np.random.randn()
    w8 = np.random.randn()
    w9 = np.random.randn()
    w10 = np.random.randn()
    b = np.random.randn()

    iterations = 10000
    learning_rate = 0.1
    costs = []  # keep costs during training, see if they go down

    for i in range(iterations):
        # get a random point
        ri = np.random.randint(len(data))
        point = data[ri]

        z = point[0] * w1 + point[1] * w2 + point[2]*w3 + point[3]*w4 + point[4]*w5 + point[5]*w6 + point[6]*w7 + point[7]*w8 + point[8]*w9 + point[9]*w10 + b
        pred = sigmoid(z)  # networks prediction

        target = point[10]

        # cost for current random point
        cost = np.square(pred - target)
        '''
        # print the cost over all data points every 1k iters
        if i % 100 == 0:
            c = 0
            for j in range(len(data)):
                p = data[j]
                p_pred = sigmoid(w1 * p[0] + w2 * p[1] + b)
                c += np.square(p_pred - p[2])
            costs.append(c)
        '''
        dcost_dpred = 2 * (pred - target)
        dpred_dz = sigmoid_p(z)

        dz_dw1 = point[0]
        dz_dw2 = point[1]
        dz_dw3 = point[2]
        dz_dw4 = point[3]
        dz_dw5 = point[4]
        dz_dw6 = point[5]
        dz_dw7 = point[6]
        dz_dw8 = point[7]
        dz_dw9 = point[8]
        dz_dw10 = point[9]
        dz_db = 1

        dcost_dz = dcost_dpred * dpred_dz

        dcost_dw1 = dcost_dz * dz_dw1
        dcost_dw2 = dcost_dz * dz_dw2
        dcost_dw3 = dcost_dz * dz_dw3
        dcost_dw4 = dcost_dz * dz_dw4
        dcost_dw5 = dcost_dz * dz_dw5
        dcost_dw6 = dcost_dz * dz_dw6
        dcost_dw7 = dcost_dz * dz_dw7
        dcost_dw8 = dcost_dz * dz_dw8
        dcost_dw9 = dcost_dz * dz_dw9
        dcost_dw10 = dcost_dz * dz_dw10

        dcost_db = dcost_dz * dz_db

        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        w3 = w3 - learning_rate * dcost_dw3
        w4 = w4 - learning_rate * dcost_dw4
        w5 = w5 - learning_rate * dcost_dw5
        w6 = w6 - learning_rate * dcost_dw6
        w7 = w7 - learning_rate * dcost_dw7
        w8 = w8 - learning_rate * dcost_dw8
        w9 = w9 - learning_rate * dcost_dw9
        w10 = w10 - learning_rate * dcost_dw10

        b = b - learning_rate * dcost_db

    return  w1, w2, b


w1, w2, b = train()
print("valor w1:", w1)
print("valor w2:", w2)
print("valor b:", b)
'''
#fig = plt.plot(costs)
z = w1 * 2 + w2 * 2.5 + b
pred = sigmoid(z)

print(pred)
'''