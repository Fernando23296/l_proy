import cv2


img = cv2.imread("ejem.jpg")

# Select ROI
r = cv2.selectROI("Image", img, False, False)

# Crop image
imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Display cropped image
cv2.imshow("Image", imCrop)
cv2.waitKey(0)
