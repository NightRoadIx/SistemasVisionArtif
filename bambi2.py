import numpy as np
import cv2

# Generar dos imágenes
img1 = np.zeros((400, 600),
                dtype=np.uint8)
img1[100:300, 200:400] = 255

img2 = np.zeros((400, 600),
                dtype=np.uint8)
img2 = cv2.circle(img2, (300, 200),
                  125, (255), -1)
# Mostrarlas
cv2.imshow('uno',img1)
cv2.imshow('dos',img2)
cv2.waitKey(0)

# Operación AND en imágenes
imgAND = cv2.bitwise_and(img1, img2)
cv2.imshow('AND',imgAND)
cv2.waitKey(0)

# Operación OR en imágenes
imgOR = cv2.bitwise_or(img1, img2)
cv2.imshow('OR',imgOR)
cv2.waitKey(0)

# Operación XOR en imágenes
imgXOR = cv2.bitwise_xor(img1, img2)
cv2.imshow('XOR',imgXOR)
cv2.waitKey(0)

# Operación NOT en imágenes
imgNOT = cv2.bitwise_not(img1)
cv2.imshow('NOT',imgNOT)
cv2.waitKey(0)

# Apertura de una image
imagen = cv2.imread('img1.png')
# Redimensionar al tamaño
imgNRedim = cv2.resize(
    imagen, (600, 400),
    interpolation = cv2.INTER_LINEAR
)
cv2.imshow('IMAGEN',imgNRedim)
cv2.waitKey(0)

# Hacer la operación AND con ambas imágenes
# Se efectúa con la imagen redimensionada
# usando como máscara la img2
# se repite dado que se coloca la imagen a operar
# y donde se guardará o la imagen destino
santo = cv2.bitwise_and(
    imgNRedim, imgNRedim,
    mask = img2
)
cv2.imshow('FINAL',santo)
cv2.waitKey(0)

