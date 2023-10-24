import cv2
import numpy as np
import matplotlib.pyplot as mp

# Se la abro... (la imagen)
img = cv2.imread('gato.jpg')
cv2.imshow('Destino',img)
cv2.waitKey(0)

# Cambiamos la imagen a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gris como vida", gris)
cv2.waitKey(0)

# Obtener el Histograma de la imagen
# Esto se obtiene mediante la función de
# OpenCV
histograma = cv2.calcHist([gris],
                          [0],
                          None,
                          [256],
                          [0, 256])
mp.plot(histograma)
mp.grid()
mp.show()

# Histograma mediante numpy
# Regresa los valores del histograma
# y los contenedores o bins, los valores del
# eje x
his, bins = np.histogram(
    gris.flatten(), 256, [0, 256]
)

# FDA (función de distribución acumulada)
# Se trata de una función que describe la probabilidad
# acumulada de que una variable aleatoria sea menor o
# igual a un valor dado.
fda = his.cumsum()
# Normalizar
fdaN = fda / fda.max()
mp.plot(fdaN)
mp.grid()
mp.show()

# Realizar el proceso de ecualización del histograma
# la función ma.masked_equal sirve para enmascarar
# un arreglo donde el valor dado es igual al valor
# del elemento del arreglo
fdaM = np.ma.masked_equal(fda, 0)
print(fdaM)
# Se busca crear una FDA que sea una línea recta
# puesto que sería una FDA de una fdp uniforme
fdaM = (fdaM-fdaM.min())*255/(fdaM.max()-fdaM.min())
fda = np.ma.filled(fdaM, 0).astype('uint8')
gris2 = fda[gris]
cv2.imshow("Ecualizada", gris2)
cv2.waitKey(0)

# Obtener el histograma de la imagen ecualizada en histograma
histo2 = cv2.calcHist([gris2], [0], None, [256], [0,256])
mp.plot(histo2)
mp.grid()
mp.show()

# Mediante OpenCV
equ = cv2.equalizeHist(gris)
cv2.imshow("No me vean asi", equ)
cv2.waitKey(0)

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
# La ecualización de forma "global" en una imagen puede
# acarrear problemas, ya que áreas con cambios bruscos
# de intensidad, la ecaulización puede exagerar el contraste
# Entonces, se propone realizar la ecualización en
# pequeños bloques de nxn, ecualizando cada bloque de manera
# individual y aplica una operación llamada "limitación de
# contraste" evitando que los valores de píxeles se extiendan
# demasiado, revisando sus valores con respecto al promedio
# del bloque o "kernel"
clahe = cv2.createCLAHE(clipLimit=2.0,
                        tileGridSize=(13, 13))
gris3 = clahe.apply(gris)
cv2.imshow("Ya vámonos", gris3)
cv2.waitKey(0)





cv2.destroyAllWindows()













