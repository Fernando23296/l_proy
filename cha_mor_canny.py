import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ex.png')

kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
erosion = cv2.erode(blurred, kernel, iterations=2)
#cv2.imshow("Image", erosion)
#cv2.waitKey(0)

imagen = erosion

#Crear un kernel de '1' de 3x3
kernel = np.ones((3, 3), np.uint8)

#Se aplica la transformacion: Morphological Gradient
transformacion = cv2.dilate(imagen, kernel, iterations=1) - cv2.erode(imagen, kernel, iterations=1)
'''
Mostrar el resultado y salir
cv2.imshow('resultado', transformacion)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

edges = cv2.Canny(transformacion, 90, 90)
plt.subplot(121), plt.imshow(transformacion, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
