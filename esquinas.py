'''
	DETECCIÓN DE ESQUINAS DE HARRIS
	Las esquinas son regiones de una imagen con una gran variabilidad en intensidad
	en todas las direcciones. En 1988, Chris Harris y Mike Stephens presentaron
	un algoritmo en el artículo "A combined Corner and Edge Detector".
	Simplemente lo que realiza es encontrar la diferencia en la intensidad para
	un desplzamiento de (u,v) en todas las direcciones.
	El artículo esta disponible en:
	https://www.semanticscholar.org/paper/A-Combined-Corner-and-Edge-Detector-Harris-Stephens/6818668fb895d95861a2eb9673ddc3a41e27b3b3
	
'''
import cv2
import numpy as np

# Se manda a llamar una imagen con bordes como un tablero de ajedrez
img = cv2.imread("sudokusmall.jpg")
# Cambiamos a escala de grises
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Aquí se hace la modificación de la imagen uint8 a tipo flotante
# pues el algoritmo así lo requiere
gray = np.float32(gray)
# Se aplica la detección de esquinas de Harris, la cual requiere:
# la imagen en escala de grises de tipo flotante
# tamaño del vecindario que se considerará para la detección (nxn)
# Parámetro de apertura del filtro derivativo de Sobel
# Parámetro libre del detector de Harris (k en la ecuación R = Det(M) - k(Tr(M))^2)
dst = cv2.cornerHarris(gray,2,3,0.04)

# La imagen resultante es dilatada
dst = cv2.dilate(dst,None)

# Se aplica un unmbral para un valor óptimo, varia de acuerdo a cada imagen
img[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()