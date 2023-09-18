import cv2
import numpy as np

# Fusión de imágenes
# Lectura de imágenes (ambas de las mismas dimensiones)
# en caso que no tengan las mismas dimensiones, hay que
# modificarlas
img1 = cv2.imread('img1.png')
cv2.imshow('uno',img1)
cv2.waitKey(0)

img2 = cv2.imread('img2.png')
cv2.imshow('dos',img2)
cv2.waitKey(0)

# Cambiar el peso de las imágenes y fusionarlas
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('Destino',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()