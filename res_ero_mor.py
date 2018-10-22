'''
FILLING AN IMAGE OF:
- RESIZE
- GRAY
- GAUSSIAN BLUR
- EROSION
- MORPH GRADIENT

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('ex.png')
width = 592
height = 792
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


img = resized

kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
erosion = cv2.erode(blurred, kernel, iterations=2)

#Cargar la mascara
imagen = erosion

#Crear un kernel de '1' de 3x3
kernel = np.ones((3, 3), np.uint8)

#Se aplica la transformacion: Morphological Gradient
transformacion = cv2.dilate(
    imagen, kernel, iterations=2) - cv2.erode(imagen, kernel, iterations=1)


#gray = cv2.cvtColor(transformacion, cv2.COLOR_BGR2GRAY)
'''
img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)



cv2.imshow("Prewitt", img_prewittx + img_prewitty)
'''
#cv2.imshow("Prewitt", transformacion)
cv2.imwrite('rem.png', transformacion)
