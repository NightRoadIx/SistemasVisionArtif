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

# Obtener las capas de color
b, g, r = cv2.split(img)

# Mostrar una de las capas de color (verde)
cv2.imshow('verde', g)
cv2.waitKey(0)
# Mostrar una de las capas de color (rojo)
cv2.imshow('rojo', r)
cv2.waitKey(0)
# Mostrar una de las capas de color (azul)
cv2.imshow('azul', b)
cv2.waitKey(0)

# Copiar la imagen
img2 = img
img2[:,:,0] = 0
img2[:,:,1] = 0
cv2.imshow('misterioso', img2)
cv2.waitKey(0)

# Cambiar RGB a gris = 2.989 * R + 0.5870 * G + 0.1140 * B

# Finalizar la ventana
cv2.destroyAllWindows()