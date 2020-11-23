"""
    En 1994 J. Shi y C. Tomasi hicieron una pequeña modificación al detector
    de esquinas de Harris en el artículo "Good features to track", en donde
    se mostraban mejores resultados.
    
    A diferencia del detector de esquinas de Harris, Shi-Tomasi propusieron
    como función de puntaje:
        R = min(lambda1, lambda2)
        
    Artpiculo: https://ieeexplore.ieee.org/document/323794
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('trapeador.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# La función goodFeaturesToTrack()
# recibe la imagen en escala de grises
# después la cantidad de esquinas que se pretende encontrar
# el nivel de calidad en el intervalo [0, 1], el cual denota la mínima calidad
# de la esquina, para la cual esta será rechazada o no
# Finalmente, la distancia euclideana mínima entre las esquinas detectadas
corners = cv2.goodFeaturesToTrack(gray,125,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()

cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
