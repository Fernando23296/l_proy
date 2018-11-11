import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)
#F = 3 + 2*X + 5*X*X
F = -0.0000000002381*X*X*X*X*X + 0.0000002801*X*X*X+X - 0.0001106 *X*X*X + 0.01543*X*X - 0.377*X + 177.4
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, F)
plt.show()
'''
VECTOR FINAL:  [[180.         190.         188.5        243.         230.66666667
  193.         159.25       182.         148.         170.33333333
  145.         124.2        124.         180.        ]
 [  0.          68.          84.5        140.         163.33333333
  202.66666667 236.5        277.14285714 306.         358.66666667
  389.         429.2        445.5        450.        ]]
altura 450
ancho 360
Ecuacion bonita:
            5             4             3           2
-2.381e-10 x + 2.801e-07 x - 0.0001106 x + 0.01543 x - 0.377 x + 177.4
'''
