import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import cv2


image = cv2.imread('ex_ppp.png')

plt.imshow(image)

coords = [0, 100, 200, 300, 400, 500, 600]

plt.plot(coords, coords, 'r--', linewidth=2)
plt.show()
