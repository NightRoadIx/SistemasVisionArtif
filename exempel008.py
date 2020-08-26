# Cargar la libreria numpy como np
import numpy as np
# Importar cv2 (la libreria del opencv)
import cv2

# Leer una imagen
img = cv2.imread('endgame.jpeg')

# Leer un pixel en particular
px = img[100, 100]
# Mostrarlo en pantalla
print(px)

# Apesar de también trabajar con un modelo de color
# RGB, las capas de color en Python están alineadas
# como BGR
# Solamente el pixel de color azul (capa 0)
azul = img[100, 0, 0]
print(azul)

# pero dado que se está utulizando la librería numpy
# esta cuenta con métodos para acceso a los pixeles
# que están más optimizados
# Acceder al mismo pixel, pero en rojo
print(img.item(100,100,2))

# para modificar el valor del pixel se puede utilizar
img.itemset((100,100,2), 100)
print(img.item(100,100,2))

# Algunas propieades de la imagen
print(img.shape)

# Total de pixeles
print("Pixeles totales: " + str(img.size))

# Tipo de imagen
print(img.dtype)

tony = img[260:450, 340:490]
img[140:330, 660:810] = tony

# Separar en cada capa de color
b, g, r = cv2.split(img)	# Se prefiere usar numpy
# y unir de nuevo
img2 = cv2.merge((b, g, r))
# o usar 
b = img[:,:,0]

img[:,:,1] = 0		# Esto pone todos los pixeles de la capa verde en 0

cv2.imshow('image', img)

# Esperar una tecla y recibirla en la variable
k = cv2.waitKey(0)
if k == 27:				# Tecla ESC
	# Finalizar la ventana
    cv2.destroyAllWindows()


