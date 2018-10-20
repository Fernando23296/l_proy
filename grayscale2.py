from matplotlib import pyplot as plt
import cv2

# Cargamos la imagen
original = cv2.imread("ex8_erosion.png")
# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (5, 5), 0)

cv2.imshow("suavizado", gauss)


cv2.waitKey(0)
