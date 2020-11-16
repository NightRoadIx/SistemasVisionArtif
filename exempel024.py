import numpy as np
import cv2

# IMAGEN ORIGINAL
img = cv2.imread('trapeador.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

# IMAGEN EN ESCALA DE GRISES
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', imgray)
cv2.waitKey(0)

# DETECTOR DE BORDES POR CANNY
edged = cv2.Canny(imgray, 200, 225)
cv2.imshow('Canny', edged)
cv2.waitKey(0)

# ENCONTRAR LOS CONTORNOS
# Debe utilizarse una copia de la imagen, ya que la función altera la imagen
edged2 = edged.copy()
# Los argumentos son: imagen, modo de recuperación de contornos y finalmente,
# el método de aproximación del contorno
# Regresa los contornos y la jerarquía de los mismos
# Cada contorno individual es un arreglo numpy de las coordenadas (x,y) de 
# los puntos frontera del objeto
# CHAIN_APPROX_SIMPLE calcula solamente 2 puntos (inicio y fin) de la línea
# que seguiría el contorno, en lugar de guardar todos los puntos de dicha
# línea, lo cual se obtiene con CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(edged2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# DIBUJAR LOS CONTORNOS
# en este caso se coloca la imagen en donde se dibujarán los contornos, 
# después se colocarán los contornos en arreglo numpy (x,y), luego el índice
# del contorno que se mostrará
# (Utilizar el modificador -1 indica, todos los contornos)
# y luego el color con el que el contorno se pintará y el espesor de la línea
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('Contornos', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
