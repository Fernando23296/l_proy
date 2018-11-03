import numpy as np

a = np.empty((10), dtype=object)
def uno(x):
    for i in range(0,5):
        x[i]=i
    

    return x


def dos(x):
    for i in range(5, 10):
        x[i] = i

    return x

one=uno(a)
two=dos(one)
print(two)