# -*- coding: utf-8 -*-
"""

@author: s_bio
"""

import cv2

# Cargar la captura de video
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Cargar el clasificador haarcascade entrenado
clasificador = cv2.CascadeClassifier('cascade.xml')

while True:
    
    # Capturar la imagen
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Obtener las detecciones que se realizan
    wed = clasificador.detectMultiScale(gray,
    scaleFactor = 6,
    minNeighbors = 101,
    minSize = (70,78))
    
    # Recorrer todas las detecciones
    for (x,y,w,h) in wed:
        # Colocar un rectángulo
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
        # Y el texto
        cv2.putText(frame,'El pollo rojo',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)
    
    # Salir con la tecla ESC
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()