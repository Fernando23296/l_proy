import cv2
import numpy as np  
from matplotlib import pyplot as plt

img = cv2.imread('diag2.jpg')

kernel = np.ones((5,5),np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
erosion = cv2.erode(blurred,kernel,iterations=2)
cv2.imshow("Image", erosion)
cv2.waitKey(0)
'''
plt.subplot(122),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.show()
'''
