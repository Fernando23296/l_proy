import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('ex5.jpg')
width = 592
height = 792
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
sobelx = cv2.Sobel(resized, cv2.CV_8U, 1, 0, ksize=5)

median = cv2.medianBlur(sobelx, 5)


cv2.imshow('resultado', median)
cv2.waitKey(0)
cv2.destroyAllWindows()
