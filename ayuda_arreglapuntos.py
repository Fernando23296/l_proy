import numpy as np
from matplotlib import pyplot as plt
import cv2
'''
imagen2 = imread('ex3.jpg')
division=12

lista=[[300., 295.66666667, 335.4, 210.81818182, 376.41666667,
  218., 233.88888889, 382., 371., 281., 334.75, 192., 300., 300.],

 [0., 82., 154.2, 194.54545455, 254.08333333, 315., 375.33333333,
 439.83333333, 494.25, 561.5, 618., 689., 696., 705.]]
img = cv2.imread('ex3.jpg', cv2.IMREAD_COLOR)
'''
lista = [[300., 295.66666667, 335.4, 210.81818182, 376.41666667,
          218., 233.88888889, 382., 371., 281., 334.75, 192., 300., 300.],

         [0., 82., 154.2, 194.54545455, 254.08333333, 315., 375.33333333,
          439.83333333, 494.25, 561.5, 618., 689., 696., 705.]]
img = cv2.imread('ex3.jpg', cv2.IMREAD_COLOR)


dimensions = img.shape
altura = img.shape[0]
ancho = img.shape[1]
print("altura: ",altura)
print("ancho: ", ancho)
width = int(ancho)
height = int(altura)

dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

fig, ax = plt.subplots()
aa = ax.imshow(resized)
x = lista[0]
y = lista[1]
y_inv = y[::-1]
plt.plot(x, y, 'ob')
plt.show()
