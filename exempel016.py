import cv2
import numpy as np
from matplotlib import pyplot as plt

# Utilizando Matplotlib
# Imprimir el histograma de una imagen (en escala de grises)
img = cv2.imread('bamel.jpg',0)
# ravel() regresa la matriz como un vector plano
# se envía el número de barras (256)
# y que intervalo se va a manejar
plt.hist(img.ravel(),256,[0,256]); plt.show()

# Para el caso de las imágenes BGR
img = cv2.imread('bamel.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    # caclHist(images, canales, máscara, histSize, ranges)
    # máscara, aplica una máscara sobre cierta porción de la imagen, si se desea obtener de toda la imagen, se coloca None
    # binSize or histSize
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()


# Utilizando openCV
img = cv2.imread('bamel.jpg',0)
# Crear una máscara
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calcular el histograma con y sin máscara
# Verificar el tercer argumento para la máscara
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, cmap = 'gray')
plt.subplot(222), plt.imshow(mask, cmap = 'gray')
plt.subplot(223), plt.imshow(masked_img, cmap = 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()