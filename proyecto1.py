import numpy as np
import imutils
import cv2

#FUNCIONA PERO LAS COORDENADAS SALEN DEL CORTE
img = cv2.imread('ex_ppp.png', cv2.IMREAD_COLOR)
dimensions = img.shape

# height, width, number of channels in image
altura = img.shape[0]
width = img.shape[1]
#print("Altura: ",altura)
#print("Ancho: ", width)
ancho=int(width)
alfa=int(altura/12)
#print(alfa)
cons=0
for i in range(1,1000):
    
    cons1=cons
    cons2=cons1+alfa
    #print(cons1)
    #print(cons2)
    print("____")
    image = img[cons1:cons2, 0:ancho]
    
    #convirtiendo a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #aplicando desenfoque gaussiano
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #threshold?
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)

    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    count=1
    for c in cnts:
        M = cv2.moments(c)
        
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        #print(cX)
        #print(cY)
        xx=str(cX)+","+str(cY)
        print(xx)
        #CONTORNO ENCONTRADO
        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
        #CIRCULO DE CENTRO
        cv2.circle(image, (cX, cY), 7, (0,0, 255), -1)
        #COORDENADAS
        cv2.putText(image, xx, (cX - 50, cY - 50),
        #TIPO DE LETRA, COLOR?
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
        #cv2.imshow("Image", image)
        #imagen=image
        #img[0:100,0:490]=imagen
        cv2.imshow("Image", img)
        count=count+1
        cv2.waitKey(0)
    cons = cons2
    i=i+1
#python center_blob1.py --image prueba1.png




