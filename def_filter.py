import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import cv2
import imutils
from operator import is_not
from functools import partial
from pylab import *
from random import *
import scipy.ndimage.morphology as morp


img = cv2.imread('pruebazzz.png')
img_2 = img

def skeletonize(img):

    struct = np.array([[[[0, 0, 0], [0, 1, 0], [1, 1, 1]],
                        [[1, 1, 1], [0, 0, 0], [0, 0, 0]]],

                       [[[0, 0, 0], [1, 1, 0], [0, 1, 0]],
                        [[0, 1, 1], [0, 0, 1], [0, 0, 0]]],

                       [[[0, 0, 1], [0, 1, 1], [0, 0, 1]],
                           [[1, 0, 0], [1, 0, 0], [1, 0, 0]]],

                       [[[0, 0, 0], [0, 1, 1], [0, 1, 0]],
                           [[1, 1, 0], [1, 0, 0], [0, 0, 0]]],

                       [[[1, 1, 1], [0, 1, 0], [0, 0, 0]],
                           [[0, 0, 0], [0, 0, 0], [1, 1, 1]]],

                       [[[0, 1, 0], [0, 1, 1], [0, 0, 0]],
                           [[0, 0, 0], [1, 0, 0], [1, 1, 0]]],

                       [[[1, 0, 0], [1, 1, 0], [1, 0, 0]],
                           [[0, 0, 1], [0, 0, 1], [0, 0, 1]]],

                       [[[0, 1, 0], [1, 1, 0], [0, 0, 0]],
                           [[0, 0, 0], [0, 0, 1], [0, 1, 1]]]])

    img = img.copy()
    last = ()
    while np.any(img != last):
        last = img
        for s in struct:
            img = np.logical_and(img, np.logical_not(
                morp.binary_hit_or_miss(img, *s)))
    return img


dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
qua = int(width/10)
qua2 = int(qua*3)
qua7 = int(qua*7)
img[0:height, 0:qua2] = [0]
img[0:height, qua7:width] = [0]

kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
erosion = cv2.erode(gray, kernel, iterations=2)

thresh = cv2.threshold(gray, 150, 75, cv2.THRESH_BINARY)[1]
img_gaussian = cv2.GaussianBlur(thresh, (3, 3), 0)
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)


img = img_prewittx + img_prewitty
ret, img = cv2.threshold(img, 172, 255, 0)
img = skeletonize(img)

#img = cv2.imread('ex1_ppp.png', cv2.IMREAD_COLOR)
dimensions = img.shape
altura = img.shape[0]
width = img.shape[1]
print(width)
ancho = int(width)
altura2 = int(altura)
alfa = int(altura/12)
cons = 0

a = np.empty((13, 50), dtype=object)
for i in range(0, 13):

    cons1 = cons
    cons2 = cons1+alfa
    print("____")
    image = img[cons1:cons2, 0:ancho]

    #convirtiendo a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #aplicando desenfoque gaussiano
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #threshold?
    thresh = cv2.threshold(blurred, 60, 200, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    count = 1
    for c in cnts:
        M = cv2.moments(c)

        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
                cX, cY = 0, 0
        xx = str(cX)+","+str(cY)
        print(i)
        a[i][count] = [cX, cY]
        print(xx)

        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
        #CIRCULO DE CENTRO
        cv2.circle(image, (cX, cY), 7, (0, 0, 255), -1)
        #COORDENADAS
        cv2.putText(image, xx, (cX - 50, cY - 50),
                    #TIPO DE LETRA, COLOR?
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        count = count+1
    cons = cons2
    i = i+1

cero = [0, 0]
b = [[cero if x is None else x for x in c] for c in a]
b = b[::-1]


def igualador(l):
    contador = 1
    for i in range(2, 13):
        for ii in range(0, 50):
            l[i][ii][1] += alfa*contador
        contador = contador+1
    return l


b = igualador(b)


def reemplazador(l):

    for u in range(1, 13):
        for uu in range(0, 50):
            if (l[u][uu][0] == 0):
                l[u][uu] = None
            else:
                pass
    return l


b = reemplazador(b)

print("altura", altura2)
print("ancho", ancho)

ax = np.zeros(shape=(13, 1), dtype=object)
contador = 0


def limpio(l):
    tam = len(l)
    a = []
    for i in range(0, tam):
        if(l[i] != None):
            a.append(l[i])
    return a


def rellenador(l, ancho, largo):
    tam = len(l)
    largo = int(largo/12)
    ancho = int(ancho/2)
    for i in range(1, tam):
        if (l[i] == []):
            relleno = [ancho, largo*i]
            l[i].append(relleno)
        else:
            pass
    return l


def seleccionador(l):
    a = []
    tam = len(l)
    for i in range(1, tam):
        tam1 = (len(l[i])-1)

        a.append(l[i][randint(0, tam1)])
    return a


lis_2 = []

for i in range(1, 13):
    a = limpio(b[i])
    lis_2.append(a)

lis_3 = []
lis_3 = rellenador(lis_2, ancho, altura2)

ax = seleccionador(lis_3)

print(ax)

ancho2 = int(ancho/2)
axx = np.asarray(ax)
bx = np.array([[ancho2, altura2]])
cx = np.concatenate((axx, bx), axis=0)
dx = np.array([[ancho2, 0]])
axx = np.concatenate((dx, cx), axis=0)
axx = np.array(axx.T)
tck, u = interpolate.splprep(axx, s=0)
unew = np.arange(0, 1.01, 0.01)
out = interpolate.splev(unew, tck)


img = plt.imread(img_2)
fig, ax = plt.subplots()
ax.imshow(img)

plt.plot(out[0], out[1], color='orange')
plt.plot(axx[0, :], axx[1, :], 'ob')
plt.show()
