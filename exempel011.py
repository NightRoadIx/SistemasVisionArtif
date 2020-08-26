import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bamel.jpg')

# # # # Escalar la imagen
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow('image',img)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)
cv2.imshow('imagen Rev',res)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

# O también se puede realizar mediante

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('imagen Rev2',res)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

# Salvar imagen
status = cv2.imwrite('miObradeArte.jpg', res)

# # # # Transladar la imagen
img = cv2.imread('bamel.jpg', 0)
rows,cols = img.shape

# Se utiliza una matriz de transformación
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('imagen tras',dst)
cv2.waitKey(0)


# # # # Rotar la imagen
# De la misma forma se tiene que utilizar una matriz de transformación
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)		# centro, angulo, escala
# Se usa una de las 2 funciones de transformación disponibles
# warpAffine(imagen, matriz 2x3, tupla con columnas y filas)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('imagen rot',dst)
cv2.waitKey(0)


# # # # Transformación de perspectiva
img = cv2.imread('sudokusmall.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

# warpPerspective(imagen, matriz 3x3, Tamaño de la imagen dst(w h))
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


cv2.destroyAllWindows()