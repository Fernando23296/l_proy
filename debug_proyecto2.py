import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import cv2
import imutils
from operator import is_not
from functools import partial
from pylab import *
from random import *


img = cv2.imread('ex1_ppp.png', cv2.IMREAD_COLOR)
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
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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

b=igualador(b)

def reemplazador(l):

    for u in range(1, 13):
        for uu in range(0, 50):
            if (l[u][uu][0] == 0):
                l[u][uu] = None
            else:
                pass
    return l
b=reemplazador(b)

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
    a=[]
    tam=len(l)
    for i in range(1,tam):
        tam1=(len(l[i])-1)
        
        a.append(l[i][randint(0, tam1)])
    return a

lis_2=[]

for i in range(1,13):
    a=limpio(b[i])
    lis_2.append(a)

lis_3=[]
lis_3 = rellenador(lis_2,ancho,altura2)

ax=seleccionador(lis_3)

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


img = plt.imread("ex1.jpg")
fig, ax = plt.subplots()
ax.imshow(img)

plt.plot(out[0], out[1], color='orange')
plt.plot(axx[0, :], axx[1, :], 'ob')
plt.show()
