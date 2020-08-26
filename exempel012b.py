import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bamel.jpg', 0)

# Aplicar un filtro2D (convolución) con una matriz
# 5x5 de 1 multiplicado por (1/25) [Normalización de la matriz]
kernel = np.ones((5,5),np.float32)/25
kernel = np.array([[-1,-1,-1],[-1, 8,-1],[-1,-1,-1]])
#kernel = np.array([[-1,-1,-1],[2, 2, 2],[-1,-1,-1]])
dst = cv2.filter2D(img,-1,kernel)
ret,umbral = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)

print(kernel)
print(ret)

plt.subplot(131),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(dst, cmap = 'gray'),plt.title('Filtrado')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(umbral, cmap = 'gray'),plt.title('Umbralizado')
plt.xticks([]), plt.yticks([])
plt.show()