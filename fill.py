import cv2
import numpy as np

img = cv2.imread("ex1_erosion.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

ret, thresh2 = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)
cv2.floodFill(thresh2, mask, (350, 250), (255, 255, 0))

thresh2 = cv2.cvtColor(thresh2, cv2.COLOR_GRAY2RGB)


thresh2[np.where((thresh2 == [0, 0, 0]).all(axis=2))] = [0, 255, 255]
thresh2[np.where((thresh2 == [255, 255, 255]).all(axis=2))
        ] = img[np.where((thresh2 == [255, 255, 255]).all(axis=2))]

cv2.imshow("img", thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
