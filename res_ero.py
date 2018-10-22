'''
FILLING AN IMAGE OF:
- RESIZE AN IMAGE
- GRAY
- GAUSSIAN BLUR
- EROSION

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('ex6.png')
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

#cv2.imshow("Prewitt", transformacion)
cv2.imwrite('re6.png', erosion)
