import numpy as np
from matplotlib import pyplot as plt

a = [[304, 4],
[310, 4],
[311, 69], 
[313, 30], 
[314, 11], 
[325, 50], 
[339, 51], 
[353, 20], 
[363, 46], 
[365, 19], 
[374, 27], 
[383, 54]]

b=[[282,20],
    [280,77],
    [278,33],
    [270,88],
    [268,53],
    [290,45],
    [320,34],
    [323,44],
    [330,45]]
plt.plot(*sum(a, []), marker='o', color='r')
plt.plot(*sum(b, []), marker='o', color='b')

plt.show()
