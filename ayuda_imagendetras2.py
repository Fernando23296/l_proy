
import numpy
import matplotlib.pyplot as plt
img = plt.imread("ex2.jpg")
fig, ax = plt.subplots()
x1 = [409.       ,   348.66666667 , 459.,          293.33333333 , 440.,
      329.83333333 , 367.11111111 , 338.83333333  ,307.,          409.,
      501.,          409.,          409.]
y1 = [0.   ,       111.83333333,  266.      ,    327.33333333  ,387.,
      481.   ,       574.    ,      683.       ,   750.       ,   810.,
      901.   ,       990.  ,       1090.]
xl=400
yl =  800
ax.imshow(img, extent=[0, xl, 0, yl])
ax.plot(x1, y1, 'r', linewidth=5, color='firebrick')
plt.show()
