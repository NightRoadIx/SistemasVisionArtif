# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:40:04 2022

@author: s_bio
"""

from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# Valor de ancho del objeto de referencia
# ancho = 0.955     # pulgadas
ancho = 24.26     # milímetros

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

# Cargar la imagen, cambiarla a escala de grises y difuminarla un poco
image = cv2.imread("referencia.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
# Realizar la detección de bordes y luego realizar la dilatación y erosión 
# para cerrar las posibles aperturas entre los bordes de los objetos
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
# Encontrar los contornos en el mapa de bordes
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# Arreglar los contornos de izquierda a derecha e iniciar la variable
# de calibración 'pixels per metric'
(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

# Iterar sobre los contornos individualmente
for c in cnts:
	# si el contorno no es suficientemente grande ignorarlo
	if cv2.contourArea(c) < 100:
		continue
	# calcular cuadro delimitador rotado del contorno
	orig = image.copy()
	box = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
	box = np.array(box, dtype="int")
    # Ordenar los puntos en el contorno para que aparezcan de la forma:
    # superior-izquierdo, superior-derechom inferior-derecho, inferior-izquierdo
    # dibujar la caja del cuadro delimitador del contorno
	box = perspective.order_points(box)
	cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
	# rotar sobre los puntos originales y dibujarlos
	for (x, y) in box:
		cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
    
    # Desempaquetar las cajas ordenadas, luego calcular el punto central
    # entre las coordenadas superior izquierda y superior derecha,
    # seguido por el punto central entre las coordenadas inferiores
	(tl, tr, br, bl) = box
	(tltrX, tltrY) = midpoint(tl, tr)
	(blbrX, blbrY) = midpoint(bl, br)
    # Calcular el punto central entre superior-inferior izquierdos
    # seguido de superior-inferior derechos
	(tlblX, tlblY) = midpoint(tl, bl)
	(trbrX, trbrY) = midpoint(tr, br)
	# dibujar los puntos medios de las imágenes
	cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
    # dibujar las líneas entre los puntos medios
	cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
		(255, 0, 255), 2)
	cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
		(255, 0, 255), 2)
    
    # calcular la distancia Euclídea entre los puntos medios
	dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
	dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    # si los pixeles por metrica no han sido iniciados, entonces
    # calcularlo como la proporción de los píxeles a la métrica proporcionada    
	if pixelsPerMetric is None:
		pixelsPerMetric = dB / ancho
        
	# calcular las dimensiones del objeto
	dimA = dA / pixelsPerMetric
	dimB = dB / pixelsPerMetric
    # Dibujar el tamaño del objeto en la imagen
	cv2.putText(orig, "{:.2f}mm".format(dimA),
		(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
	cv2.putText(orig, "{:.2f}mm".format(dimB),
		(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
	# Mostrar la imagen de salida
	cv2.imshow("Image", orig)
	cv2.waitKey(0)

cv2.destroyAllWindows()