# RELLENO EN UNA IMAGEN CON CUADRADOS
import numpy as np  
import cv2
import imutils

img = cv2.imread('ex_ppp.png',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
'''
a = 10
b=10
c = 10
xx = 1
'''

#a=img[37:111, 107:194]
#gray_image = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
#img[0:74,0:87]=gray_image

'''
watch_face = img[37:111,107:194]
rotated = imutils.rotate(watch_face, 180)
img[0:74,0:87]=rotated

dimensions = img.shape

# height, width, number of channels in image
altura = img.shape[0]
width = img.shape[1]
ancho = int(width)
alfa = int(altura/12)
print(alfa)
'''


#puntos pequeños
img[79:81, 354:356] = [0, 255, 0]
img[76:78, 343:345] = [0, 255, 255]


img[125:127, 361:363] = [0, 255, 255]

'''
#eje y, eje x
img[100:300, 0:200] = [0, 0, 255]
img[200:600, 0:300] = [255, 0, 0]
img[100:500, 100:800] = [255, 0, 255]
'''
'''
gray[100:300, 0:200] = [0]
gray[200:600, 0:300] = [0]
gray[100:500, 100:800] = [0]
'''
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

