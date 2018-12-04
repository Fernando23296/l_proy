#TRAZAR UNA RECTA

import matplotlib.pyplot as plt

x = [-4, 2]
y =[-3, 5]

x1=x[0]
y1=y[0]

x2=x[1]
y2=y[1]


sum=((x2-x1)**2)+((y2-y1)**2)
print(sum)
dis=sum**0.5
print(dis)
plt.plot(x, y, marker = 'o')
plt.show()