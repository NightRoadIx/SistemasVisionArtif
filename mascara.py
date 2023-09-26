import numpy as np
import cv2

# Apertura de una imagen
imagen = cv2.imread('gato.jpg')
fondo = cv2.imread('santa.png')

# Características de la imagen a la que le queremos montar
imgC = imagen.shape

# Reducir el tamaño de la imagen a montar
fondo2 = cv2.resize(fondo, (100,100), cv2.INTER_CUBIC)
fndC = fondo2.shape
print(fndC)

# Montar la imagen
# [filas, columnas, colores]
#imagen[:fndC[0], :fndC[1], :] = fondo2
cv2.imshow("Original", imagen)
cv2.waitKey(0)

# ROI (Region Of Interest)
# RDI
# Región en donde reside nuestro interés XD
iniX = 570
iniY = 180
roi = imagen[iniY:iniY+fndC[0], iniX:iniX+fndC[1], :]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Cambiamos la imagen a montar a escala de grises
fondoGris = cv2.cvtColor(fondo2, cv2.COLOR_BGR2GRAY)
# Crear a una máscara a partir del umbral
ret, mask = cv2.threshold(fondoGris, 20, 255, cv2.THRESH_BINARY)
cv2.imshow("Máscara", mask)
cv2.waitKey(0)

#A esta imagen se lo sacamos... el negativo
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("Máscara Negada", mask_inv)
cv2.waitKey(0)

# Usar el stencil
imagen_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow("Stencil", imagen_bg)
cv2.waitKey(0)

# "Coloriar" el stencil
imagen_fg = cv2.bitwise_and(fondo2, fondo2, mask=mask)
cv2.imshow("Stencil con color", imagen_fg)
cv2.waitKey(0)

# Hacer el mix
# dst = cv2.add(imagen_bg, imagen_fg)
dst = cv2.addWeighted(imagen_bg, 0.6, imagen_fg, 0.4, 0.0)
cv2.imshow("Mix de imágenes", dst)
cv2.waitKey(0)

# Pos ahí les va el remix
# Poner en la imagen
imagen[iniY:iniY+fndC[0], iniX:iniX+fndC[1], :] = dst
cv2.imshow("Final", imagen)
cv2.waitKey(0)


cv2.destroyAllWindows()
