import numpy as np
import imutils
import cv2
from matplotlib import pyplot as plt
from operator import is_not
from functools import partial
from pylab import *


#FUNCIONA PERO LAS COORDENADAS SALEN DEL CORTE
img = cv2.imread('ex_ppp.png', cv2.IMREAD_COLOR)
dimensions = img.shape

# height, width, number of channels in image
altura = img.shape[0]
width = img.shape[1]
print(width)
#print("Altura: ",altura)
#print("Ancho: ", width)
ancho = int(width)
alfa = int(altura/12)
#print(alfa)
cons = 0

#a = np.chararray((20, 50))
#a = np.zeros(shape=(13, 50))
a = np.empty((13, 50), dtype=object)
for i in range(1, 13):

    cons1 = cons
    cons2 = cons1+alfa
    #print(cons1)
    #print(cons2)
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
        '''
        y = (cX,cY)
        yy = np.asarray(y)
        print(y)
        print(i)
        a[i][count]=np.append(np.int_([cX, cY]))
        '''
        print(i)
        #a[i][count] = np.array([cX,cY])
        a[i][count] = [cX, cY]
        '''
        numpy.array([1.2, "abc"], dtype=object)
        a[i][count] = np.array([cX, cY], dtype=object)
        beta = np.array([cY])
        a[i][count] = np.append(a[i][count], beta)
        print(type(xx))
        '''

        print(xx)
        #print(c)

        #print(i)  # grande

        #print(count)#pequeño
        #print(xx)

        #CONTORNO ENCONTRADO
        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
        #CIRCULO DE CENTRO
        cv2.circle(image, (cX, cY), 7, (0, 0, 255), -1)
        #COORDENADAS
        cv2.putText(image, xx, (cX - 50, cY - 50),
                    #TIPO DE LETRA, COLOR?
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        #cv2.imshow("Image", image)
        #imagen=image
        #img[0:100,0:490]=imagen
        #cv2.imshow("Image", img)

        count = count+1

    cons = cons2
    i = i+1

cero=[0,0]
b = [[cero if x is None else x for x in c] for c in a]

print(alfa)
print(b[12][:])
print("*"*10)
contador=1
for i in range(1,13):
    for ii in range(0,50):
        b[i][ii][1]+=alfa*contador
    contador=contador+1

for u in range(1,13):
    for uu in range(0,50):
        if (b[u][uu][0]==0):
            b[u][uu] = None
        else:
            pass

print(b[12][:])
print("*"*10)

_1 = b[1][:]
_1 = np.asarray(_1)
_1 = _1[_1 != np.array(None)]
_1 = _1.tolist()
_1 = np.asarray(_1)

_2 = b[2][:]
_2 = np.asarray(_2)
_2 = _2[_2 != np.array(None)]
_2 = _2.tolist()
_2 = np.asarray(_2)

_3 = b[3][:]
_3 = np.asarray(_3)
_3 = _3[_3 != np.array(None)]
_3 = _3.tolist()
_3 = np.asarray(_3)

_4 = b[4][:]
_4 = np.asarray(_4)
_4 = _4[_4 != np.array(None)]
_4 = _4.tolist()
_4 = np.asarray(_4)

_5 = b[5][:]
_5 = np.asarray(_5)
_5 = _5[_5 != np.array(None)]
_5 = _5.tolist()
_5 = np.asarray(_5)

_6 = b[6][:]
_6 = np.asarray(_6)
_6 = _6[_6 != np.array(None)]
_6 = _6.tolist()
_6 = np.asarray(_6)

_7 = b[7][:]
_7 = np.asarray(_7)
_7 = _7[_7 != np.array(None)]
_7 = _7.tolist()
_7 = np.asarray(_7)

_8 = b[8][:]
_8 = np.asarray(_8)
_8 = _8[_8 != np.array(None)]
_8 = _8.tolist()
_8 = np.asarray(_8)

_9 = b[9][:]
_9 = np.asarray(_9)
_9 = _9[_9 != np.array(None)]
_9 = _9.tolist()
_9 = np.asarray(_9)

_10 = b[10][:]
_10 = np.asarray(_10)
_10 = _10[_10 != np.array(None)]
_10 = _10.tolist()
_10 = np.asarray(_10)

_11 = b[11][:]
_11 = np.asarray(_11)
_11 = _11[_11 != np.array(None)]
_11 = _11.tolist()
_11 = np.asarray(_11)

_12 = b[12][:]
_12 = np.asarray(_12)
_12 = _12[_12 != np.array(None)]
_12 = _10.tolist()
_12 = np.asarray(_12)

x, y = _8.T
print(_8)
plt.plot(x, y, 'bo')
plt.show()


'''
_1=a[1][:]
_1 = _1[_1 != np.array(None)]

print (_1[1][:])
print (_1[1][2])

aa = a[9][:]

print(a)
b = aa[aa != np.array(None)]
bb = b.tolist()
print(bb)
bb = np.asarray(bb)
x, y = bb.T
#plt.plot(x, y)
#plt.show()
plt.plot(x, y, 'bo')
plt.show()
'''
