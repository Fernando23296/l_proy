import cv2
import numpy as np


def erodeDilate(imagePath):
    # Read the input image
    frame = cv2.imread('diag6.png')

    # kernel is used to control the amount of eroding and dilating
    kernel = np.ones((5, 5), np.uint8)

    # Repeat the erosion and dilation by changing iterations.
    img_erode = cv2.erode(frame, kernel, iterations=2)
    img_dilate = cv2.dilate(frame, kernel, iterations=2)

    cv2.imshow('Input', frame)
    cv2.imshow('Erosion', img_erode)
    cv2.imshow('Dilation', img_dilate)
    cv2.waitKey(0)


def main():
    imagePath = 'hanif.jpg'
    erodeDilate(imagePath)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
