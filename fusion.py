#%%
import cv2
import numpy as np

# Abrir imagen 1
img1 = cv2.imread('colibri.jpg',-1)
# Abrir una ventana con la imagen
cv2.imshow('imagen1', img1)
# Esperar una tecla
cv2.waitKey(0)

# Abrir imagen 2
img2 = cv2.imread('colibri01.jpg',-1)
# Abrir una ventana con la imagen
cv2.imshow('imagen2', img2)
# Esperar una tecla
cv2.waitKey(0)

# Modificar el tamaño de ambas imágenes
# a 512x512
img1R = cv2.resize(img1, (512, 512), 
                 interpolation = cv2.INTER_CUBIC)
img2R = cv2.resize(img2, (512, 512), 
                 interpolation = cv2.INTER_CUBIC)
# Abrir una ventana con la imagen
cv2.imshow('imagen1', img1R)
# Esperar una tecla
cv2.waitKey(0)
# Abrir una ventana con la imagen
cv2.imshow('imagen2', img2R)
# Esperar una tecla
cv2.waitKey(0)

# Cambiar y fusionar las imágenes
dst = cv2.addWeighted(img1R, 0.7, img2R, 0.3, 0)
# Abrir una ventana con la imagen
cv2.imshow('fusion', dst)
# Esperar una tecla
cv2.waitKey(0)

cv2.destroyAllWindows()