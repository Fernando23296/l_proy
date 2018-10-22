import cv2
import numpy as np


img = cv2.imread('skel.png')

thresh = cv2.threshold(img, 200, 200, cv2.THRESH_BINARY)[1]
cv2.imshow("skel", thresh)

cv2.waitKey(0)


'''
img = cv2.blur(img, (5, 5))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

thresh0 = cv2.adaptiveThreshold(
    s, 50, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
thresh1 = cv2.adaptiveThreshold(
    v, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
thresh2 = cv2.adaptiveThreshold(
    v, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
thresh = cv2.bitwise_or(thresh0, thresh1)

cv2.imshow('Image-thresh0', thresh0)
cv2.waitKey(0)
cv2.imshow('Image-thresh1', thresh1)
cv2.waitKey(0)
cv2.imshow('Image-thresh2', thresh2)
cv2.waitKey(0)
'''
