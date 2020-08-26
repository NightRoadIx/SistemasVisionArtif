import cv2
import numpy as np
# from matplotlib import pyplot as plt

# Leer la imagen
img = cv2.imread('dave.jpg',0)
# Obtener la imagen al aplicarle un filtro
# de mediana 
img_filter = cv2.medianBlur(img,5)

cv2.imshow('Original', img)
cv2.imshow('Filtrada', img_filter)
k = cv2.waitKey()

# Obtener una imagen umbralizada  de forma binaria con valores de 127 a 255
ret,th1 = cv2.threshold(img_filter,127,255,cv2.THRESH_BINARY)
cv2.imshow('Filtrada umbralizada', th1)
k = cv2.waitKey()

# Valor del umbralizado es el promedio del área del vecindario
# (imagen, valor máximo, método, tipo de umbralizado, tamaño_bloque, constate)
# El valor del umbral T(x,y) es el promedio de tamaño_bloque x tamaño_bloque de (x,y) menos C
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
cv2.imshow('Filtrada umbralizada adaptativa por promedio', th2)
k = cv2.waitKey()

# en este caso es una suma ponderada (correlación cruzada con una ventana Gaussiana) del tamaño_bloque x tamaño_bloque
# del vecindario (x,y) menos C. La sigma (desviación estándar) es utilizada como el tamaño_bloque
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
cv2.imshow('Filtrada umbralizada adaptativa gaussiano', th3)
k = cv2.waitKey()

cv2.destroyAllWindows()