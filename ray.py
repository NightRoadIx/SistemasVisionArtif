import cv2
import numpy as np
import matplotlib.pyplot as mp

# Se la abro... (la imagen)
img = cv2.imread('gato.jpg')

# Características de la imagen
alto, ancho, _ = img.shape

# Estoy bien idiota d ela p a la o
# olvide pasar la imagen a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Luego lo pongo todo como cuando me pongo bien grifo
borroso = cv2.GaussianBlur(gris, (9, 9), 0)

sobelX = cv2.Sobel(borroso, cv2.CV_64F, 1, 0, ksize=3)
sobelY= cv2.Sobel(borroso, cv2.CV_64F, 0, 1, ksize=3)

# Umbralizacionisación
ret, umbral = cv2.threshold(sobelX, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("Veo borroso en X", sobelX)
cv2.imshow("Veo borroso en Y", sobelY)
cv2.waitKey(0)

cv2.destroyAllWindows()
