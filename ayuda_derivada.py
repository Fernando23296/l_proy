from scipy.ndimage import rotate
from scipy.misc import imread, imshow
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import cv2
import imutils
from operator import is_not
from functools import partial
from pylab import *
from random import *
from sklearn.cluster import KMeans
from matplotlib import transforms

#de aqui para abajo es todo girado

y=[180.     ,    207.     ,    232.    ,     218.      ,   230.66666667,
 212.    ,     159.25   ,    182.    ,     170.6      ,  153.33333333,
 155.     ,    223.75   ,    213.    ,     180.]
print("_"*20)
print(y)
print("_"*20)
x=[0.     ,     56.   ,      105.     ,    141.      ,   163.33333333,
 216.33333333 ,236.5  ,      277.14285714 ,310.8   ,     340.33333333,
 396.5     ,   427.75    ,   444.5      ,  450.]

'''

y = [300.       ,  252.    ,     228.    ,     196.   ,      215.66666667,
     281.       ,  329.6  ,      293.88888889, 341. ,        353.,
     332.85714286,245.75   ,    221.    ,     300.]
x = [0.       ,   65.       ,  151.   ,      205.25  ,     247.33333333,
     323.75     ,  379.8    ,    435.44444444 ,493.33333333 ,544.,
     604.71428571, 677.6875  ,   701.5    ,    705.]
'''
'''
y = [409.      ,   381.5   ,     326.     ,    374.33333333 ,343.,
     347. ,        379.    ,     402.  ,       457.     ,   517.,
     520.5   ,     509.5      ,  539.    ,     409.]
x = [0.       ,   149.5     ,    241.5  ,       284.     ,     404.,
     509.       ,   606.33333333 , 642.66666667 , 800.   ,       861.5,
     942.     ,    1012.5      ,  1084.       ,  1090.]
'''

#ejemplo ex5.png
x=[  0.      ,    68. ,        105.     ,    141.   ,      163.33333333,
 202.66666667, 236.5       , 274.25    ,   310.8    ,    358.66666667,
 396.5     ,   429.2   ,     445.5     ,   450.        ]
y=[180.  ,       190.     ,    232.     ,    218.     ,    230.66666667,
 193. ,        159.25      , 154.     ,    170.6    ,    170.33333333,
 155.    ,     124.2   ,     124.   ,      180.        ]

print("_"*20)

print(x)
print("_"*20)
def polinomial(x,y):
    z = np.polyfit(x, y, 5)
    #print(z)
    #print('.-.-'*30)
    f = np.poly1d(z)
    #print("Ecuacion bonita: ")
    #print(f)
    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 50)

    x_new2 = x_new[::-1]

    y_new = f(x_new2)
    y_new = y_new[::-1]
    return (x_new2,y_new)
xx,yy=polinomial(x,y)
def max_min(x,y):
    z = np.polyfit(x, y, 5)
    #print(z)
    #print('.-.-'*30)
    f = np.poly1d(z)
    #print("Ecuacion bonita: ")
    #print(f)
    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 50)

    x_new2 = x_new[::-1]

    y_new = f(x_new2)
    y_new = y_new[::-1] #LO GIRAMOS
    #a=f*10000000000

    prim=f.deriv(1)
    segu = f.deriv(2)
    lroot=np.roots(prim)
    lroot2=[]
    for i in lroot:
        lroot2.append(segu(i))
    lroot3=[]
    for ii in lroot:
        lroot3.append(f(ii))

    xdev= lroot[::-1]
    ydev=lroot3

    return xdev,ydev
print("___"*20)

a,b=max_min(x,y)
print(a)
print("___"*20)
print(b)
plt.plot(a,b, 'or')



'''
esto da bien
plt.plot(324.148, 229.3530, 'ob')
plt.plot(126.688, 158.2289, 'ob')
'''
the_plot = plt.plot(xx, yy)
plt.show()

