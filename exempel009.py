import cv2
import numpy as np

# Lectura de imagenes
img1 = cv2.imread('mabel6.png')
img2 = cv2.imread('bamel.jpg')

# Cambiar el peso de las imágenes
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

# Mostrarlas
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()