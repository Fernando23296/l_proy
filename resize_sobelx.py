import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('ex.png')
width = 592
height = 792
dim = (width, height)

# resize image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(gray, dim, interpolation=cv2.INTER_AREA)
sobelx = cv2.Sobel(resized, cv2.CV_8U, 1, 0, ksize=5)

cv2.imwrite('rs.png', sobelx)
'''

print('Resized Dimensions : ', sobelx.shape)

cv2.imshow("Resized image", sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
