import numpy
from matplotlib import pyplot, transforms
'''
data = [
        [1,1],
        [2,2],
        [3,3],
        [4,4],
        [5,5],
        [6,6]]
'''
x=[1,2,3,4,5]
y = [1, 2, 3, 4, 5]
# first of all, the base transformation of the data points is needed
base = pyplot.gca().transData
rot = transforms.Affine2D().rotate_deg(90)

# define transformed line
line = pyplot.plot(x,y, 'r', transform=rot + base)
# or alternatively, use:
# line.set_transform(rot + base)

pyplot.show()
