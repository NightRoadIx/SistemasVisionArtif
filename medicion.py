import numpy as np
import cv2

# Lectura de la imagen
image = cv2.imread("chessboard2.png")
cv2.imshow('Original', image)
cv2.waitKey(0)

# Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Escala de grises', gray)
cv2.waitKey(0)

# Aplicar un filtro Gaussiano
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow('Gaussiana', gray)
cv2.waitKey(0)

# Generar el detector de bordes por Canny
edged = cv2.Canny(gray, 50, 100)
cv2.imshow('Canny', edged)
cv2.waitKey(0)

# Dilatar la imagen, esto genera que los bordes detectados
# se "expandan"
# La operación consiste en convolucionar la imagen con un kernel
edged = cv2.dilate(edged, None, iterations=1)
cv2.imshow('Dilatada', edged)
cv2.waitKey(0)

# Erosionar la imagen, esto disminuye los bordes
# dilatados en el paso anterior, lo que elimina los dobles bordes
# que por lo general Canny genera
edged = cv2.erode(edged, None, iterations=1)
cv2.imshow('Erosionada', edged)
cv2.waitKey(0)