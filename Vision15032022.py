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

# Aplicar los filtros
laplaciano = cv2.Laplacian(imggris, cv2.CV_8U)
# Los filtros Sobel van a funcionar para revisar líneas tanto horizontales
# como verticales
sobelx = cv2.Sobel(imggris, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(imggris, cv2.CV_64F, 0, 1, ksize=5)

# Abrir una ventana con la imagen
cv2.imshow('Laplaciano', laplaciano)
# Esperar una tecla
cv2.waitKey(0)

# Abrir una ventana con la imagen
cv2.imshow('Sobel x', sobelx)
# Esperar una tecla
cv2.waitKey(0)

# Abrir una ventana con la imagen
cv2.imshow('Sobel y', sobely)
# Esperar una tecla
cv2.waitKey(0)

cv2.destroyAllWindows()

#%%

gauss = cv2.GaussianBlur(imggris, (5, 5), 0)
# Abrir una ventana con la imagen
cv2.imshow('imagenGauss', gauss)
# Esperar una tecla
cv2.waitKey(0)

img_median = cv2.medianBlur(imggris, 5)

# Detector de contornos de Canny
# Desarrollado John F. Canny en 1986
# imagen, umbral_inferior, umbral_superior
canny = cv2.Canny(imggris, 150, 200)

# Abrir una ventana con la imagen
cv2.imshow('Canny', canny)
# Esperar una tecla
cv2.waitKey(0)

#%%
# Transformaciones morfológicas
import numpy as np
# Erosión
# Crear un kernel de nxn
kernelE = np.ones((5,5), np.uint8)
erision = cv2.erode(canny, kernelE, iterations = 1)
# Abrir una ventana con la imagen
cv2.imshow('Erosionada', erision)
# Esperar una tecla
cv2.waitKey(0)

# Dilatación
dilacion = cv2.dilate(canny, kernelE, iterations = 1)
# Abrir una ventana con la imagen
cv2.imshow('Dilatada', dilacion )
# Esperar una tecla
cv2.waitKey(0)

cv2.destroyAllWindows()