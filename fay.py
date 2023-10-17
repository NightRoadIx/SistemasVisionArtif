import cv2
import numpy as np
import matplotlib.pyplot as plt

# Se la abro... (la imagen)
img = cv2.imread('gato.jpg')
cv2.imshow('Destino',img)
cv2.waitKey(0)


# Se las separamos a la imagen
b, g, r = cv2.split(img)
# Aplicar umbralizados
ret, bU = cv2.threshold(b, 150, 255, cv2.THRESH_BINARY)
ret, gU = cv2.threshold(g, 120, 255, cv2.THRESH_BINARY)
ret, rU = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)

# Fusionar
img2 = cv2.merge((bU, gU, rU))
cv2.imshow('Destiny',img2)
cv2.waitKey(0)

# Aplicación mortal del mundo mundial
# Obtenemos la escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Hacemos la imagen más borrosa
gauss = cv2.GaussianBlur(gris,(9,9),0)
# Enmascaramos
# Umbralizar
ret, mascarita = cv2.threshold(
    gauss, 100, 255, cv2.THRESH_BINARY)
# Lo hacemos, le aplicamos la operación AND
final = cv2.bitwise_and(
    img, img, mask=mascarita
)
cv2.imshow("CajaNegra", final)
cv2.waitKey(0)


# Pajamo' ahora a e'pacio HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Cortar en un intervalo
# Mantener en el intervalo [0, 30] Hue
mascara = cv2.inRange(imgHSV, (0,50,50), (30,255,255))
final2 = cv2.bitwise_and(img, img, mask=mascara)

from scipy import ndimage as nd
# Obtener la máscara binaria, pasando un kernel de 7x7
maskCerrada = nd.binary_closing(mascara, np.ones((7,7)))
plt.imshow(maskCerrada)
plt.show()

# pip install scikit-image
from skimage import io, measure
etiquetaNegra = measure.label(maskCerrada)
print(np.unique(etiquetaNegra))
plt.imshow(etiquetaNegra)
plt.show()

from skimage.color import label2rgb
img2 = label2rgb(etiquetaNegra, image=img)
plt.imshow(img2)
plt.show()

cv2.destroyAllWindows()





