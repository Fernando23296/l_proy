import numpy as np
import imutils
import cv2

#FUNCIONA PERO LAS COORDENADAS SALEN DEL CORTE
image = cv2.imread('esc1.png', cv2.IMREAD_COLOR)

#convirtiendo a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #aplicando desenfoque gaussiano
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #threshold?
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)




cv2.imshow("image", cnts)
cv2.waitKey(0)
cv2.destroyAllWindows()
