'''
FILLING AN IMAGE OF:
- RESIZE
- GRAY
- GAUSSIAN BLUR
- EROSION
- FILLING AN IMAGE

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils


img = cv2.imread('ex5.jpg')
width = 592
height = 792
qua=int(width/6)
qua7=int(qua*5)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


img = resized

kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
erosion = cv2.erode(blurred, kernel, iterations=2)

erosion[0:height, 0:qua] = [0]
erosion[0:height, qua7:width] = [0]
#erosion[90:200, 0:50] = [255, 0, 0]
#erosion[10:100, 0:50] = [255, 0, 255]
#cv2.imshow("Prewitt", transformacion)
cv2.imwrite('ref5.png', erosion)

'''
cv2.imshow('image', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
