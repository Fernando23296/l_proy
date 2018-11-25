from scipy.ndimage import rotate
from scipy.misc import imread, imshow
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import cv2
import imutils
from operator import is_not
from functools import partial
from pylab import *
from random import *
from sklearn.cluster import KMeans
from matplotlib import transforms
import scipy.ndimage.morphology as morp
from skimage import feature

fuente = 'ex2.jpg'
img = cv2.imread(fuente, cv2.IMREAD_COLOR)
imagen2 = imread(fuente)
height = img.shape[0]
width = img.shape[1]
qua = int(width/10)
qua2 = int(qua*3)
qua7 = int(qua*7)
#img[0:height, 0:qua2] = [0]
#img[0:height, qua7:width] = [0]

kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 198, 300, cv2.THRESH_BINARY)[1]
edges2 = feature.canny(thresh, sigma=3)

#skel = skeletonize(thresh)

#nombre = nombre_archivo(fuente)
#nuevo_nombre = nombre+'_gts.png'
#cv2.imshow('sd', skel.astype(np.uint8)*255)
archivo = 'ex2_gray.png'

nuevo_nombre = 'bruno.png'
cv2.imwrite(nuevo_nombre, edges2)
cv2.imshow("gray", edges2)

cv2.waitKey(0)



'''
#del ex2
[[], 
[[341, 117], [345, 85]], 
[[339, 151]], [[256, 253]], 
[[237, 346], [243, 301]], 
[[237, 350], [235, 354]], 
[[250, 485], [306, 481], [246, 449]], 
[[266, 548], [323, 542], [311, 493], [257, 499]], 
[[304, 623], [292, 624], [329, 612], [272, 606], [325, 598], [264, 562]], 
[[294, 680], [343, 668], [349, 670], [274, 659], [321, 661], [304, 631]], 
[[326, 764], [320, 762], [252, 760], [306, 742], [319, 731], [330, 713], [267, 710]], 
[[174, 834], [328, 802], [238, 809], [333, 776], [323, 777], [247, 773]], 
[[168, 907], [184, 903], [384, 893], [299, 878], [247, 875], [390, 865], [216, 862], [168, 880], [180, 877], [300, 845], [175, 843], [169, 845]], 
[[392, 911], [385, 911], [180, 911], [167, 910]]]

'''
