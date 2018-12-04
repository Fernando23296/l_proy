
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")import matplotlib
    from matplotlib import pyplot as plt
    from matplotlib import transforms
from scipy.ndimage import rotate
from scipy.misc import imread, imshow
import numpy as np

from scipy import interpolate
import cv2
import imutils
from operator import is_not
from functools import partial
from pylab import *
from random import *
from sklearn.cluster import KMeans

import scipy.ndimage.morphology as morp
fuente = 'ex2.png'
img = cv2.imread(fuente, cv2.IMREAD_COLOR)
imagen2 = imread(fuente)
division=13

'''
FUNCIONES
'''

def nombre_archivo(na):
        punto = na.find(".")
        b = ''
        for i in range(0, punto):
                b += str(na[i])
        return b

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

def igualador(l):
    contador = 1
    for i in range(1, (division+1)):
        for ii in range(0, 50):
            l[i][ii][1] += alfa*contador
        contador = contador+1
    return l


def reemplazador(l, div):
    #AQUI SE CAMBIO EL 1 DEL RANGE, ANTES ERA 2-------------------------------------
    for u in range(0, (div+1)):
        for uu in range(0, 50):
            if (l[u][uu][0] == 0):
                l[u][uu] = None
            else:
                pass
    return l


def limpio(l):
    tam = len(l)
    a = []
    for i in range(0, tam):
        if(l[i] != None):
            a.append(l[i])
    return a


def rellenador(l, div, ancho, largo):
    tam = len(l)
    largo = int(largo/div)
    ancho = int(ancho/2)
    for i in range(0, tam):
        if (l[i] == []):
            relleno = [ancho, largo*i]
            l[i].append(relleno)
        else:
            pass
    return l


def seleccionador(l):
    a = []
    tam = len(l)
    for i in range(0, tam):
        tam1 = (len(l[i])-1)

        a.append(l[i][randint(0, tam1)])
    return a


def seleccionador_kmeans(l):
    tam = len(l)
    xpro = []
    for i in range(0, tam):

        tam1 = len(l[i])
        x1 = np.array([])
        x1 = l[i]
        tam2 = len(x1)
        if (tam2 == 1):
            k = 1

            kmeans = KMeans(k)
            # Fitting the input data
            kmeans = kmeans.fit(x1)
            # Getting the cluster labels
            labels = kmeans.predict(x1)
            # Centroid values
            centroids = kmeans.cluster_centers_
            # Comparing with scikit-learn centroids
            #print(C)  # From Scratch
            xpro.append(centroids[0])
        else:
            k = 2

            kmeans = KMeans(k)
            # Fitting the input data
            kmeans = kmeans.fit(x1)
            # Getting the cluster labels
            labels = kmeans.predict(x1)
            # Centroid values
            centroids = kmeans.cluster_centers_
            # Comparing with scikit-learn centroids
            #print(C)  # From Scratch
            xpro.append(centroids[randint(0, 1)])
    return xpro


def max_min(x, y):
    z = np.polyfit(x, y, 5)
    #print(z)
    #print('.-.-'*30)
    f = np.poly1d(z)
    #print("Ecuacion bonita: ")
    #print(f)
    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 50)

    x_new2 = x_new[::-1]

    y_new = f(x_new2)
    y_new = y_new[::-1]  # LO GIRAMOS
    #a=f*10000000000

    prim = f.deriv(1)
    segu = f.deriv(2)
    lroot = np.roots(prim)
    lroot2 = []
    for i in lroot:
        lroot2.append(segu(i))
    lroot3 = []
    for ii in lroot:
        lroot3.append(f(ii))

    xdev = lroot[::-1]
    ydev = lroot3

    return xdev, ydev


def punto_inflexion(x, y):
    z = np.polyfit(x, y, 5)
    f = np.poly1d(z)
    print('ecuacion bonita')
    print(f)
    segu = f.deriv(2)
    print('segunda derivada', segu)
    lrootx = np.roots(segu)
    print("esto es lrootx: ",lrootx)
    lrooty = []
    for i in lrootx:
        lrooty.append(f(i))
    print("esto es lrooty: ",lrooty)
    return lrootx, lrooty

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
thresh = cv2.threshold(gray, 198, 300, cv2.THRESH_BINARY)[1]

skel = skeletonize(thresh)

nombre= nombre_archivo(fuente)
nuevo_nombre= nombre+'_gts.png'
cv2.imwrite(nuevo_nombre, skel.astype(np.uint8)*255)


img = cv2.imread(nuevo_nombre)
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
ancho = int(width)
altura = int(height)
alfa = int(altura/division)
cons = 0
a = np.empty(((division+1), 50), dtype=object)

for i in range(0, (division+1)):

    cons1 = cons
    cons2 = cons1+alfa
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
        a[i][count] = [cX, cY]

        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
        #CIRCULO DE CENTRO
        cv2.circle(image, (cX, cY), 7, (0, 0, 255), -1)
        #COORDENADAS
        cv2.putText(image, xx, (cX - 20, cY - 20),
                    #TIPO DE LETRA, COLOR?
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow("Image", img)
        count = count+1

    cons = cons2
    i = i+1

cero = [0, 0]
b = [[cero if x is None else x for x in c] for c in a]
#b = b[::-1]

b = igualador(b)

b = reemplazador(b, division)
ax = np.zeros(shape=((division+1), 1), dtype=object)
contador = 0

lis_2 = []

for i in range(0, (division+1)):
    a = limpio(b[i])
    lis_2.append(a)

lis_3 = []
lis_3 = rellenador(lis_2, division, ancho, altura)
ax = seleccionador_kmeans(lis_3)

#print("Lista: ", ax)

ancho2 = int(ancho/2)
axx = np.asarray(ax)
bx = np.array([[ancho2, altura]])
cx = np.concatenate((axx, bx), axis=0)
dx = np.array([[ancho2, 0]])

if (ax[0][1] < alfa):
    axx = np.concatenate((dx, cx), axis=0)
    axx = np.delete(axx, 1, 0)
    axx = np.array(axx.T)
else:
    axx = np.array(cx.T)

#print("VECTOR FINAL: ", axx)
#print("altura", altura)
#print("ancho", ancho)

dim = (ancho, altura)
resized = cv2.resize(imagen2, dim, interpolation=cv2.INTER_AREA)


plt.imshow(resized)
l_x = axx[0]
l_x = l_x.tolist()
l_y = axx[1]
l_y = l_y.tolist()

plt.plot(l_x, l_y, 'ob')
#plt.plot(axx[0, :], axx[1, :], 'ob')
plt.show()


#de aqui para abajo es todo girado
y = axx[0]
#print("_"*30)
#print(y)
#print("_"*30)
x = axx[1]
#print("_"*30)
#print(x)
#print("_"*30)


#print("___"*20)
pi1, pi2 = punto_inflexion(x, y)
#print("+++"*20)
a, b = max_min(x, y)
a_2 = a[1:3]
b_2 = b[1:3]
#print(a)
#print("___"*20)
#print(b)


z = np.polyfit(x, y, 5)
f = np.poly1d(z)

#print("Ecuacion bonita: ")
#print(f)
# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
x_new2 = x_new[::-1]

y_new = f(x_new2)
y_new = y_new[::-1]
img2 = rotate(imagen2, -90)

width = altura

height = ancho
dim = (width, height)
resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

fig, ax = plt.subplots()
aa = ax.imshow(resized)


# height, width, number of channels in image
altura = img.shape[0]
width = img.shape[1]
y_grafo = y
#print(type(y_grafo))
#CABECERA
y_inv = y[::-1]

#plt.plot(x,y_inv, 'ob')
#plt.plot(324.148, 229.3530, 'ob')
#plt.plot(126.688, 158.2289, 'ob')
#plt.plot(319, 216, 'ob')
#print("_"*20)
#print(x_new2)
#print("_"*20)
#print(y_new)
plt.plot(a_2, b_2, 'or')
plt.plot(pi1, pi2, 'oy')
the_plot = plt.plot(x_new2, y_new)


plt.savefig('debug_proyecto3.png')
plt.show()
