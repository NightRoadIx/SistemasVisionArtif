#%%
import cv2
import numpy as np


# Abrir imagen
img1 = cv2.imread('colibri.jpg',-1)
# Abrir una ventana con la imagen
cv2.imshow('imagen1', img1)
# Esperar una tecla
cv2.waitKey(0)

# Cambiar a escala de grises
imggris = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# Abrir una ventana con la imagen
cv2.imshow('imagen en gris', imggris)
# Esperar una tecla
cv2.waitKey(0)

# Generar un kernel
# Matriz NxN (N de preferencia que sea impar)
# Kernel identidad
kernel1 = np.array(
    [[2,-1,-1],
     [-1,2,-1],
     [-1,-1,2]
     ]
    )
# Umbral
T = 10

gauss = cv2.GaussianBlur(src = imggris, ksize = (9,9), sigmaX = 0, sigmaY = 0)
# Abrir una ventana con la imagen
cv2.imshow('imagenGauss', gauss)
# Esperar una tecla
cv2.waitKey(0)

# Aplicar Laplaciano
laplacian = cv2.Laplacian(gauss, cv2.CV_8U)
# Abrir una ventana con la imagen
cv2.imshow('imagenLaplaciano', laplacian)
# Esperar una tecla
cv2.waitKey(0)

ret,novaLap = cv2.threshold(laplacian,T,255,cv2.THRESH_BINARY)
# Abrir una ventana con la imagen
cv2.imshow('imagenConKernel', novaLap)
# Esperar una tecla
cv2.waitKey(0)


# Aplican el kernel a la imagen
imgg2 = cv2.filter2D(src = imggris, ddepth = -1, kernel = kernel1)
# Abrir una ventana con la imagen
cv2.imshow('imagenConKernel', imgg2)
# Esperar una tecla
cv2.waitKey(0)

# Pasar por el umbral
ret,nova = cv2.threshold(imgg2,T,255,cv2.THRESH_BINARY)
ret,nova2 = cv2.threshold(imgg2,T,255,cv2.THRESH_BINARY_INV)
ret,nova3 = cv2.threshold(imgg2,T,255,cv2.THRESH_TRUNC)
ret,nova4 = cv2.threshold(imgg2,T,255,cv2.THRESH_TOZERO)
ret,nova5 = cv2.threshold(imgg2,T,255,cv2.THRESH_TOZERO_INV)
# Abrir una ventana con la imagen
cv2.imshow('imagenUmbral', nova)
# Esperar una tecla
cv2.waitKey(0)
# Abrir una ventana con la imagen
cv2.imshow('imagenUmbral', nova2)
# Esperar una tecla
cv2.waitKey(0)
# Abrir una ventana con la imagen
cv2.imshow('imagenUmbral', nova3)
# Esperar una tecla
cv2.waitKey(0)
# Abrir una ventana con la imagen
cv2.imshow('imagenUmbral', nova4)
# Esperar una tecla
cv2.waitKey(0)
# Abrir una ventana con la imagen
cv2.imshow('imagenUmbral', nova5)
# Esperar una tecla
cv2.waitKey(0)

cv2.destroyAllWindows()