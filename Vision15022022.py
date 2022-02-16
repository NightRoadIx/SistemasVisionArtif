# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:51:41 2022

@author: s_bio
"""

# Importar cv2 (la libreria del opencv)
import cv2

# Leer una imagen, el 0 indica que en color gris
# Para este caso se usa una imagen JPG
img = cv2.imread('colibri.jpg',-1)
# Abrir una ventana con la imagen
cv2.imshow('image', img)
# Esperar una tecla
cv2.waitKey(0)

# Obtener las características de la imagen
ancho, alto, capas =  img.shape

# Cambiar RGB a gris 
# La operación matemática que lo efectua es la siguiente:
# gris = 2.989 * R + 0.5870 * G + 0.1140 * B
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', gris)
cv2.waitKey(0)

#%%
# Aquí cortamos la imagen en 4 cuadrantes y obtenemos el primero
# o si lo vemos en formato del plano cartesiano sería el II

# obtener el tamaño de la imagen en gris
anchog, altog = img.shape
# Se corta
cortada = gris[0:int(anchog/2), 0:int(altog/2)]
cv2.imshow('cortada', cortada)
cv2.waitKey(0)

# AHORA SU TAREA, SI DECIDEN ACEPTARLA, ES CORTAR LA IMAGEN EN 16
# CUADROS Y DISTRIBUIRLOS ALEATORIAMENTE
cortada = gris[0:int(ancho/4), 0:int(alto/4)]
cv2.imshow('cortada', cortada)
cv2.waitKey(0)

# Finalizar la ventana
cv2.destroyAllWindows()