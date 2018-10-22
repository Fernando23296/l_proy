# FILE OF EROSION, THRESHOLD (150,200) AND PREWITT (PREWITTX+PREWITTY)
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('ex1.jpg')

kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
erosion = cv2.erode(gray, kernel, iterations=2)

thresh = cv2.threshold(gray, 150, 200, cv2.THRESH_BINARY)[1]
img_gaussian = cv2.GaussianBlur(thresh, (3, 3), 0)
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

#cv2.imshow("Prewitt", transformacion)
#cv2.imwrite('ero_prex5.png', img_prewittx + img_prewitty)
cv2.imshow("ero_pre", img_prewittx + img_prewitty)


cv2.waitKey(0)
cv2.destroyAllWindows()
