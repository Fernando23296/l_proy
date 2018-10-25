from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(0, 10, num=11, endpoint=True)
#y = np.cos(-x**2/9.0)
x = [35,54,41,25,37,49]
y= [23,43,56,33,68,21]

print(x)
print(y)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 10, num=41, endpoint=True)

plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
