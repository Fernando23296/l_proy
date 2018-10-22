import cv2
import numpy as np


img = cv2.imread('ex4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#parece buena opcion
#thresh = cv2.threshold(gray, 150, 200, cv2.THRESH_BINARY)[1]

#parece buena opcion tambien
#thresh = cv2.threshold(gray, 200, 50, cv2.THRESH_BINARY)[1]

#parece buena opcion tambien tambien
thresh = cv2.threshold(gray, 150, 50, cv2.THRESH_BINARY)[1]
img_gaussian = cv2.GaussianBlur(thresh, (3, 3), 0)

#canny
img_canny = cv2.Canny(thresh, 100, 200)

#sobel
img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

#cv2.imwrite('sobelx.png', img_sobelx + img_sobely)
cv2.imwrite('prewittx.png', img_prewittx + img_prewitty)
cv2.imshow("Original Image", img)
cv2.imshow("Canny", img_canny)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)


'''
CON BLURRED
img = cv2.imread('ex2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
img_gaussian = cv2.GaussianBlur(blurred, (3, 3), 0)

#canny
img_canny = cv2.Canny(blurred, 100, 200)

#sobel
img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

#cv2.imwrite('prewitt2.png', img_prewittx + img_prewitty)
cv2.imshow("Original Image", img)
cv2.imshow("Canny", img_canny)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
