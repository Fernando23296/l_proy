import numpy as np
import skimage
from skimage import data, io, filters
from skimage.filters import gaussian
import cv2
image = cv2.imread('ex.png')


def imshow(image):
    io.imshow(image)
    io.show()




def blur(image, x0, x1, y0, y1, sigma=1, imshowall=False):
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    im = image.copy()
    sub_im = im[x0:x1, y0:y1].copy()
    if imshowall:
        imshow(sub_im)
    blur_sub_im = gaussian(sub_im, sigma=sigma)
    if imshowall:
        imshow(blur_sub_im)
    blur_sub_im = np.round(255 * blur_sub_im)
    im[x0:x1, y0:y1] = blur_sub_im
    return im


filtered_img = blur(image, 10, 600, 300, 1000, sigma=20)
imshow(filtered_img)
