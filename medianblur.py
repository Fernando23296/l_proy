import cv2
import numpy as np

img = cv2.imread("esc_dilate.png")
final = cv2.medianBlur(img, 3)
cv2.imshow("Image", img)
