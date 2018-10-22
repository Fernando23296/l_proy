#FILE FOR CHANGE A CONTRAST A IMAGE
import cv2

img = cv2.imread('ex1.jpg')  # load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert it to hsv

h, s, v = cv2.split(hsv)
v += 255
final_hsv = cv2.merge((h, s, v))

img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("image_processed2.jpg", img)
