
import cv2

img = cv2.imread('ex8_erosion.png', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

width = 592
height = 792
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
