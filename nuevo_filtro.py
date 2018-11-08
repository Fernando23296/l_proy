import scipy.ndimage.morphology as morp
import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt

#Cargar la mascara
#da perfecto para todos menos ex4.jpg
img = cv2.imread('ex4.png')

#Crear un kernel de '1' de 3x3
kernel = np.ones((3, 3), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 195, 300, cv2.THRESH_BINARY)[1]
#Se aplica la transformacion: Morphological Gradient
'''transformacion = cv2.dilate(
    thresh, kernel, iterations=3) - cv2.erode(thresh, kernel, iterations=1)
'''
#Mostrar el resultado y salir
cv2.imshow('resultado', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
