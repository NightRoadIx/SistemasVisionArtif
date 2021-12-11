# -*- coding: utf-8 -*-
"""

@author: s_bio
"""

# Cargar todas las librerías a utilizar
import cv2
import numpy as np
import imutils
import os

#%%
# En esta sección se genera la carpeta donde se guardarán las
# imágenes del entrenamiento
Datos = 'n'
if not os.path.exists(Datos):
    print('Carpeta creada en ' + os.getcwd() + "\\" + Datos)
    os.makedirs(Datos)

#%%
# Cargar la captura de video
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Obtener el tamaño de la imagen a tomar
anch = int(cap.get(3))
alto = int(cap.get(4))

# Se crea un rectángulo para considerar de la imagen
x1, y1 = 180, 70
x2, y2 = anch - 180, alto - 70

count = 0
while True:
    
    # Leer cuadro por cuadro
    ret, frame = cap.read()
    # En caso de que algo falle en la captura de imágenes, salir
    if ret == False: break
    # Obtener una copia de la imagen capturada
    imAux = frame.copy()
    # Dibujar el rectángulo donde se colocará la imagen
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    
    # Obtener la parte donde se muestra el objeto
    objeto = imAux[y1:y2,x1:x2]
    # Cambiar el tamaño de la imagen a uno pequeño
    objeto = imutils.resize(objeto,width=38)
       
    # Obtener la tecla presionada
    k = cv2.waitKey(1)
    # En caso de que se presione una 's' guardar la imagen
    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
        print('Imagen guardada:'+'/objeto_{}.jpg'.format(count))
        count = count +1
    # Con la tecla ESC se sale del programa
    if k == 27:
        break
    
    # Mostrar las imágenes de la cámara
    cv2.imshow('frame',frame)
    # y el objeto
    cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()