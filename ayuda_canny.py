import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage import feature
import cv2

# Generate noisy image of a square
im = cv2.imread('ex3.jpg', 0)
# Compute the Canny filter for two values of sigma
edges1 = feature.canny(im)
edges2 = feature.canny(im, sigma=4.5)


plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges2, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
