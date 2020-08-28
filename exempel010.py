import cv2
import numpy as np

# Abrir dos imágenes
img1 = cv2.imread('trapeador.jpg') # Esta será la imagen base
img2 = cv2.imread('logo3.png') # Esta será la imagen del logo (de tamaño menor)

# Se desea colocar un logo en la esquina superior izquierda, por lo que se genera una ROI (Region Of Image, Región de la Imagen)
rows,cols,channels = img2.shape
print(img2.shape)
roi = img1[0:rows, 0:cols]


# Crear una máscara con el logo y creae su máscara inversa
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grigio',img2gray)
cv2.waitKey(0)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
print(ret)
print(mask)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Grigio inversa',mask_inv)
cv2.waitKey(0)

# Oscurecer el área del logo en la ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('Sin espacio del logo',img1_bg)
cv2.waitKey(0)

# Mostrar solo la región del logo de la imagen del logo
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('Región del logo',img2_fg)
cv2.waitKey(0)

# Colocar el logo en la ROI y modificar la imagen original
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols] = dst

# Mostrar el resultado
cv2.imshow('Final',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
