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

img = sobelx
edges = cv2.Canny(img, 100, 1500)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
