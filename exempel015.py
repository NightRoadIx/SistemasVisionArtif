'''
	DETECCIÓN DE BORDES POR CANNY
	El algoritmo de detección de bordes de Canny fue desarrollado
	en 1986 por John F. Canny en el MIT.
	Se trata d eun algortimo por pasos:
	
	1.- Reducción de ruido. Como la detección de bordes es susceptible
	al ruido, lo primero que hace el algoritmo es reducir el ruido con un
	filtro Gaussiano de 5x5.
	
	2.- Hallar el gradiente de intensidad de una imagen. Se halla la derivada
	en dirección x & en dirección y para encontrar el gradiente en cada dirección.
	Posteriormente, con ambas matrices, se puede hallar la dirección de cada pixel
	de acuerdo a:
	BordeDelGradiente(G) = Sqrt(Gx^2 + Gy^2)
	Angulo(theta) = arctan(Gy/Gx)
	La dirección del gradiente siempre es perpendicular a los bordes. Se redondea a uno
	de los cuatro ángulos que rperesenten las direcciones vertical, horizontal y diagonales
	
	3.- Se hace un análisis de la imagen para suprimir los no-máximos, esto es
	se remueven todos los pixeles que no constituyen un borde.
	
	4.-Umbralización por histéresis. Este paso decide cuales son realmente bordes, usando
	dos valores umbral. Todos los valores por encima del umbral máximo son ejes, todos por debajo
	del valor mínimo no son ejes, mientras que los valores entre ambos umbrales se descartan
	dependiendo de su conectividad con los píxeles adyacentes.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagen.jpg',0)
# Aquí se usa la función Canny que trae ambos umbrales
edges = cv2.Canny(img,200,250)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Imagen de los bordes'), plt.xticks([]), plt.yticks([])

plt.show()