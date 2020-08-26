import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bamel.jpg', 0)

# Aplicar un filtro2D (convolución) con una matriz
# 5x5 de 1 multiplicado por (1/25) [Normalización de la matriz]
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst, cmap = 'gray'),plt.title('Promediado')
plt.xticks([]), plt.yticks([])
plt.show()


# Emborronamiento de las imágenes
# Se usa filtrado pasabajas para eliminar ruido de alta frecuencia (el más común)
blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur, cmap = 'gray'),plt.title('Emborronada')
plt.xticks([]), plt.yticks([])
plt.show()

# Filtrado Gaussiano
blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur, cmap = 'gray'),plt.title('Filtro Gaussiano')
plt.xticks([]), plt.yticks([])
plt.show()

# Filtro de mediana
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


noise_img = sp_noise(img,0.05)
median = cv2.medianBlur(noise_img, 5)

plt.subplot(131),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(noise_img, cmap = 'gray'),plt.title('Ruidosa')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(median, cmap = 'gray'),plt.title('Filtro de mediana')
plt.xticks([]), plt.yticks([])
plt.show()


# Filtro bilateral
blateral = cv2.bilateralFilter(img, 9, 75, 75)
plt.subplot(121),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blateral, cmap = 'gray'),plt.title('Filtro Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()