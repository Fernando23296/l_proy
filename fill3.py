import cv2

img = cv2.imread('diag3_erosion.png')

# Get original size of image
print('Original Dimensions: ', img.shape)

# Percentage of the original size
scale_percent = 220

width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize/Scale the image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# The new size of the image
print('Resized Dimensions: ', resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
