import cv2
import numpy as np

# Cargar la imagen
img1 = cv2.imread('imagen.jpg')

# Reducir el tamaño de la imagen
ancho = int(img1.shape[1] * 0.5)
alto = int(img1.shape[0] * 0.5)
img2 = cv2.resize(img1, (ancho, alto), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Imagen',img2)
cv2.waitKey(0)

# Convolución espacial
# convertir a escala de grises
gris = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris',gris)
cv2.waitKey(0)

# Aplicar un filtro2D (convolución)
# Se genera primero un kernel, que es una matriz
# MxN la cual se convolucionará con la imagen
# para obtener una nueva
# El kernel en este caso está normalizado
kernel = np.ones((5,5), np.float32)/25
# Convolución imagen con kernel
# el -1 mantiene la profundidad de bits (8 bits)
dst = cv2.filter2D(gris, -1, kernel)
cv2.imshow('Conv2D',dst)
cv2.waitKey(0)

# kernel2
# Kernel para detección de puntos
kernel2 = np.array(
    [[-1,-1,-1],
     [-1,8,-1],
     [-1,-1,-1]]
)
laBarata = cv2.filter2D(gris,-1,kernel2)
cv2.imshow('Detector de puntos',laBarata)
cv2.waitKey(0)
# Para mostrar la imagen de mejor manera se utiliza un
# valor umbral para "binarizar" la imagen
# Se utiliza la función threshold, la cual recibe
# la image, el valor umbral, el valor máximo de los pixeles
# y el método de umbralización, en este caso binaria que
# envía todos los valores por debajo del umbral a 0 y todos por
# encima a 1
# La función regresa si se logró hacer el umbralizado y la imagen
# umbralizada
ret,umbral = cv2.threshold(laBarata, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('Detector puntos umbralizado',laBarata)
cv2.waitKey(0)

cv2.destroyAllWindows()



