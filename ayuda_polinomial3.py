
'''
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 450, 360, endpoint=True)
#y = (a * (x * x)) + (b * x) + c
y = (-0.0000000002381*(x*x*x*x*x)) + (0.0000002801*(x*x*x*x)) + (0.0001106*(x*x*x)) + (0.01543*(x*x)) - (0.377*x) + 177.4
plt.plot(x, y, '-g', label=r'$y = 3x^2 + 4x + 2$')

axes = plt.gca()
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([y.min(), y.max()])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Curve')
plt.legend(loc='upper left')

plt.show()
'''
x = 422.44897959
y = -(0.0000000003738 *(x*x*x*x*x))+ (0.0000003815*(x*x*x*x)) - (0.0001257 *(x*x*x)) + (0.01356 *(x*x)) - (0.1207*x ) + 179.3
print(y)
