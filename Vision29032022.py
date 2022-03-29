# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 01:58:24 2022

@author: s_bio
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Creamos el objeto de captura de la cámara
cap = cv2.VideoCapture(0)

while(True):
    # Capturar cuadro por cuadro
    # ret -> si se logro tomar la fotografía
    # frame -> el cuadro
    ret, frame = cap.read()
    
    # Si se logro tomar una captura
    if ret:
        # --Las operaciones que se hacen en el frame--
        # En este caso se hace que lo capturado este en escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        
        # Calcular el histograma
        # imagen, #canales, máscara, niveles_x, intervalo_niveles
        histograma = cv2.calcHist([gray], [0], None, [256], [0, 256])
        # Umbralización global o estática
        ret,nova = cv2.threshold(gray,130,255,cv2.THRESH_BINARY)
        
        # Umbralización por método de Otsu
        ret,nova2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # Umbralización por método de Otsu + Filtrado
        ret,nova3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        
        # Mostrar el frame resultante
        cv2.imshow('RGB', frame)
        cv2.imshow('Gris', gray)
        cv2.imshow('Umbral', nova)
        cv2.imshow('UmbralOtsu', nova2)
        cv2.imshow('UmbralOtsuGuassiano', nova3)
        
        #plt.plot(histograma)
        #plt.show()

        
    else:
        print("Ocurrió algún error mortal")
        break
    
    # La salida es mediante la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Una vez hecho todo, se tiene que liberar la captura de datos
cap.release()
cv2.destroyAllWindows()