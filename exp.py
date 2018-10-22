import cv2
import numpy as np
from skimage.morphology import opening

image = cv2.imread('kernel.png', 0)
kernel = np.ones((16, 16), np.uint8)

opening_opencv = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

opening_skimage = opening(image, kernel)

cv2.imwrite('opening_opencv.png', opening_opencv)
cv2.imwrite('opening_skimage.png', opening_skimage)
