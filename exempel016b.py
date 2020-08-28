import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

# Obtener la FDA del histograma
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.subplot(121)
plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.subplot(122)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histograma'), loc = 'upper left')
plt.show()

# Ecualizar el histograma
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

'''
hist,bins = np.histogram(img2.flatten(),256,[0,256])
cdf_normalized = cdf * hist.max()/ cdf.max()
'''

plt.subplot(121)
plt.imshow(img2, cmap = 'gray'),plt.title('Ecualizada')
plt.subplot(122)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histograma'), loc = 'upper left')
plt.show()


# Usando OpenCV
img = cv2.imread('dave.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow('Ecualizadas', res)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)



# Ecualización del Histograma Adpatativo Limitado por Contraste (CLAHE)

# Crear un objeto CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('CLAHE', cl1)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)
