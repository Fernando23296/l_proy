import scipy
from scipy import ndimage
import numpy as np  
import cv2
from matplotlib import pyplot as plt
from pylab import *
#x = [ 421.25571634 ,426.25279224 ,431.24986815 ,436.24694405, 441.24401995, 446.24109586]

#y = [ 0.02931459,0.03093554,  0.03563261,  0.03440331,  0.03535223,  0.03594375]
#coeffs = numpy.polyfit(x, y, 5)
#ffit = numpy.poly1d(coeffs)
#print(coeffs)
'''
para ex2
y=[282, 260, 278, 267, 278, 263 ,290, 282]
x=[0, 260 ,315 ,416 ,606, 674, 718, 915]

y=[282, 209, 356, 254, 280, 242, 263, 281, 282]
x=[0,  71, 144, 374, 498, 575, 674, 745, 915]

y=[282, 215, 356, 198, 241, 245, 267, 268 ,338, 290, 282]
x=[0 , 56, 144, 194, 302, 324, 416, 561, 627, 718, 915]
'''

# calculate polynomial
z = np.polyfit(x, y, 5)
f = np.poly1d(z)
print (f)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

img = cv2.imread('exx2.png')
width = 915
height = 564
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

fig, ax = plt.subplots()
aa=ax.imshow(resized)


# height, width, number of channels in image
altura = img.shape[0]
width = img.shape[1]
the_plot=plt.plot(x, y, 'o', x_new, y_new)


plt.show()
