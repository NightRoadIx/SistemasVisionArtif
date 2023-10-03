# ESTEGANOGRAFÍA
import cv2
import numpy as np

# Se la abro... (la imagen)
img = cv2.imread('gato.jpg')
cv2.imshow('Destino',img)
cv2.waitKey(0)
# Tamaño de la imagen
imgTam = img.shape
print(imgTam)

# Abrir imagen a esconder
hid = cv2.imread("pelos.jpg")
# Tamaño de la imagen
hidTam = hid.shape
# Cambiar a gris
hidGris = cv2.cvtColor(hid, cv2.COLOR_BGR2GRAY)
# Cambiar tamaño
hidGris = cv2.resize(hidGris, (imgTam[1],imgTam[0]),
                     cv2.INTER_LINEAR)
# Umbralizar (convertir a binario)
ret, hid2 = cv2.threshold(hidGris, 127, 255, cv2.THRESH_BINARY)
# Recorrer los bits de la imagen 7 posiciones a la derecha
# Esto deja toda la información en el bit menos significativo
# y tal cual, una imagen binaria que toma valores de 0 o 1
hid3 = hid2 >> 7
# Para mostrar hay que multiplicar por 255 ya que los valores
# son solamente 0 o 1
cv2.imshow('Escondida', hid3*255)
cv2.waitKey(0)

# REGRESAR A LA IMAGEN ORIGINAL
# Cambiar a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Lo mismo pero en gris',gris)
cv2.waitKey(0)

# Aplicar la operación AND
# con 0b11111110 para "apagar" el bit menos significativo
gus = gris & 0b11111110
cv2.imshow('Lo mismo pero mas barato', gus)
cv2.waitKey(0)
# Luego para esconder la imagen
# imagen original con el bit 0 apagado OR oculta recorrida 7 posiciones
# OR realiza una suma de conjuntos
final = gus | hid3
cv2.imshow('FBI CIA KGP INTERPOL MI6',final)
cv2.waitKey(0)

# A ver dijo el pelos
# Recorrer la imagen 7 posiciones a la izquierda
# lo cual manda el bit menos significativo a la posición
# del más significativo
recupera = final << 7
cv2.imshow('UPIIH',recupera)
cv2.waitKey(0)

cv2.destroyAllWindows()