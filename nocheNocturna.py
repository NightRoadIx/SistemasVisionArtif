import cv2
import numpy as np
import matplotlib.pyplot as plt

# Se la abro... (la imagen)
img = cv2.imread('gato.jpg')
cv2.imshow('Destino',img)
cv2.waitKey(0)

# Umbralización adaptativa
# Cambiamos a gris
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gris como vida", gris)
cv2.waitKey(0)

# Umbralización global
ret, umbral1 = cv2.threshold(gris, 127, 255,
                             cv2.THRESH_BINARY
                             )
cv2.imshow("Umbral", umbral1)
cv2.waitKey(0)

# Umbralización KKK adaptativa
umbral2 = cv2.adaptiveThreshold(
    gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11, 2
)
cv2.imshow("umbral2", umbral2)
cv2.waitKey(0)

# Umbralización KKK adaptativa2
umbral3 = cv2.adaptiveThreshold(
    gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)
cv2.imshow("umbral3", umbral3)
cv2.waitKey(0)

# Umbralización (amarilla) método de Otsu
ret, umbral4 = cv2.threshold(
    gris, 0, 255,
    cv2.THRESH_BINARY+cv2.THRESH_OTSU
)
cv2.imshow("Oxxo", umbral4)
cv2.waitKey(0)

# Aplicar la máscara
mask = cv2.bitwise_and(img, img, mask=umbral4)
cv2.imshow("Believer", mask)
cv2.waitKey(0)


cv2.destroyAllWindows()












