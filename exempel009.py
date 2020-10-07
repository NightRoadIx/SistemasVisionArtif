import cv2
import numpy as np

# Lectura de imágenes
img1 = cv2.imread('mabel6.png')
cv2.imshow('uno',img1)
cv2.waitKey(0)

img2 = cv2.imread('bamel.jpg')
cv2.imshow('dos',img2)
cv2.waitKey(0)

# Negar la imagen mediante la operación lógica NOT
'''
    NOT |0|0|1|0|0|0|0|0| = |1|1|0|1|1|1|1|1|
'''
img1_inv = cv2.bitwise_not(img1)
cv2.imshow('onu',img1_inv)
cv2.waitKey(0)

# Cambiar a escala de grises
img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('gris',img2gray)
cv2.waitKey(0)

# Cambiar el peso de las imágenes
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

# Mostrarlas
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
