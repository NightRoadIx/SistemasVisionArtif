import cv2
import numpy as np
#from matplotlib import pyplot as plt

# Leer la imagen
img = cv2.imread('trapeador.jpg',0)
cv2.imshow('Original', img)
k = cv2.waitKey()

# Umbralización global
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Umbralizacion', th1)
k = cv2.waitKey()

# Umbralización por Otsu
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Umbralizacion Otsu', th2)
k = cv2.waitKey()

# Obtención de umbralización Otsu tras filtrado Gaussiano
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Umbralizacion Otsu Gaussiano', th3)
k = cv2.waitKey()

cv2.destroyAllWindows()