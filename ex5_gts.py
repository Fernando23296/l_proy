'''
FILLING AN IMAGE OF:
- FILLING AN IMAGE
- GRAY
- THRESHOLDING (195,300)
- SKELETONIZE

'''
import scipy.ndimage.morphology as morp
import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt


def skeletonize(img):

    struct = np.array([[[[0, 0, 0], [0, 1, 0], [1, 1, 1]],
                        [[1, 1, 1], [0, 0, 0], [0, 0, 0]]],

                       [[[0, 0, 0], [1, 1, 0], [0, 1, 0]],
                        [[0, 1, 1], [0, 0, 1], [0, 0, 0]]],

                       [[[0, 0, 1], [0, 1, 1], [0, 0, 1]],
                           [[1, 0, 0], [1, 0, 0], [1, 0, 0]]],

                       [[[0, 0, 0], [0, 1, 1], [0, 1, 0]],
                           [[1, 1, 0], [1, 0, 0], [0, 0, 0]]],

                       [[[1, 1, 1], [0, 1, 0], [0, 0, 0]],
                           [[0, 0, 0], [0, 0, 0], [1, 1, 1]]],

                       [[[0, 1, 0], [0, 1, 1], [0, 0, 0]],
                           [[0, 0, 0], [1, 0, 0], [1, 1, 0]]],

                       [[[1, 0, 0], [1, 1, 0], [1, 0, 0]],
                           [[0, 0, 1], [0, 0, 1], [0, 0, 1]]],

                       [[[0, 1, 0], [1, 1, 0], [0, 0, 0]],
                           [[0, 0, 0], [0, 0, 1], [0, 1, 1]]]])

    img = img.copy()
    last = ()
    while np.any(img != last):
        last = img
        for s in struct:
            img = np.logical_and(img, np.logical_not(
                morp.binary_hit_or_miss(img, *s)))
    return img


img = cv2.imread('ex2.png')

dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
qua = int(width/10)
qua2 = int(qua*3)
qua7 = int(qua*7)
img[0:height, 0:qua2] = [0]
img[0:height, qua7:width] = [0]

kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 195, 300, cv2.THRESH_BINARY)[1]

skel = skeletonize(thresh)

cv2.imwrite('ex22_gts.png', skel.astype(np.uint8)*255)
cv2.imshow("skel", skel.astype(np.uint8)*255)

cv2.waitKey(0)
