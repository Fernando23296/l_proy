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
from matplotlib import  transforms

img = cv2.imread('ex5_gts.png', cv2.IMREAD_COLOR)
imagen2 = imread('ex5.png')
division=12


dimensions = img.shape
altura = img.shape[0]
width = img.shape[1]
ancho = int(width)
altura2 = int(altura)
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


def igualador(l):
    contador = 1
    for i in range(1, (division+1)):
        for ii in range(0, 50):
            l[i][ii][1] += alfa*contador
        contador = contador+1
    return l

b=igualador(b)

def reemplazador(l,div):
    #AQUI SE CAMBIO EL 1 DEL RANGE, ANTES ERA 2-------------------------------------
    for u in range(0, (div+1)):
        for uu in range(0, 50):
            if (l[u][uu][0] == 0):
                l[u][uu] = None
            else:
                pass
    return l
b=reemplazador(b,division)
ax = np.zeros(shape=((division+1), 1), dtype=object)
contador = 0

def limpio(l):
    tam = len(l)
    a = []
    for i in range(0, tam):
        if(l[i] != None):
            a.append(l[i])
    return a


def rellenador(l,div, ancho, largo):
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
    a=[]
    tam=len(l)
    for i in range(0,tam):
        tam1=(len(l[i])-1)
        
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


lis_2=[]

for i in range(0, (division+1)):
    a=limpio(b[i])
    lis_2.append(a)

lis_3=[]
lis_3 = rellenador(lis_2,division,ancho,altura2)

ax=seleccionador_kmeans(lis_3)

print("Lista: ",ax)

ancho2 = int(ancho/2)
axx = np.asarray(ax)
bx = np.array([[ancho2, altura2]])
cx = np.concatenate((axx, bx), axis=0)
dx = np.array([[ancho2, 0]])

if (ax[0][1]<alfa):
    axx = np.concatenate((dx, cx), axis=0)
    axx=np.delete(axx, 1, 0)
    axx = np.array(axx.T)
else: 
    axx = np.array(cx.T)

print("VECTOR FINAL: ",axx)
print("altura",altura2)
print("ancho", ancho)

dim = (ancho,altura2)
resized = cv2.resize(imagen2, dim, interpolation=cv2.INTER_AREA)

fig, ax = plt.subplots()
plt.imshow(resized)
l_x=axx[0]
l_x=l_x.tolist()
l_y = axx[1]
l_y = l_y.tolist()

plt.plot(l_x,l_y, 'ob')
#plt.plot(axx[0, :], axx[1, :], 'ob')
plt.show()


#de aqui para abajo es todo girado
y=axx[0]
x=axx[1]
z = np.polyfit(x, y, 5)
f = np.poly1d(z)

print("Ecuacion bonita: ", f)
# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
x_new2 = x_new[::-1]

y_new = f(x_new2)
y_new = y_new[::-1]
img2 = rotate(imagen2, -90)

width = altura2
height = ancho
dim = (width, height)
resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

fig, ax = plt.subplots()
aa = ax.imshow(resized)


# height, width, number of channels in image
altura = img.shape[0]
width = img.shape[1]
y_grafo=y
print(type(y_grafo))
#CABECERA
y_inv = y[::-1]
plt.plot(x,y_inv, 'ob')

#plt.plot(319, 216, 'ob')

the_plot = plt.plot( x_new2, y_new)


plt.savefig('ejemplo.png')
plt.show()



