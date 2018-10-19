import numpy as np
import cv2

#Cargar la mascara
imagen = cv2.imread('esc_erosion.png', 0)

#Crear un kernel de '1' de 3x3
kernel = np.ones((3, 3), np.uint8)

#Se aplica la transformacion: Opening
transformacion = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)

#Mostrar el resultado y salir
cv2.imshow('resultado', transformacion)
cv2.waitKey(0)
cv2.destroyAllWindows()
