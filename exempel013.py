import cv2
import random
import numpy as np

img = cv2.imread('j.png',0)

cv2.imshow('Imagen Original',img)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

# # # # # # Transformaciones morfológicas

# Erosión
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

cv2.imshow('Erosion',erosion)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)


# Dilatación
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('Dilatación',dilation)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

# Apertura
# Función para añadir ruido sal y pimienta a una imagen
def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


noise_img = sp_noise(img,0.01)
cv2.imshow('Imagen Ruidosa',noise_img)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Apertura',opening)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)


# Cerradura
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Cerradura',closing)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)


# Gradiente morfológico
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Gradiente Morfologico',gradient)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)