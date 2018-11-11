#from numpy.polynomial import Polynomial as P
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
y = [180.,    207.,    232.,     218.,   230.66666667,
     212.,     159.25,    182.,     170.6,  153.33333333,
     155.,    223.75,    213.,     180.]

x = [0.,     56.,      105.,    141.,   163.33333333,
     216.33333333, 236.5,      277.14285714, 310.8,     340.33333333,
     396.5,   427.75,   444.5,  450.]
p = np.polyfit(x, y, 5)
print(p)
segu = p.deriv(2)
print(segu)
print((segu).roots())
