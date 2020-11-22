"""
    La corrección gamma puede ser utilizada para corregir el brillo de una 
    imagen al utilizar una transformación no lineal entre los valores de
    entrada y los valores de salida mapeados:
    
        O = ((I / 255)**gamma) * 2500
        
    Dado que esta relación es no lineal, el efecto no será el mismo para todos
    los pixeles y dependerá del valor original.
    
    Cuando gamma < 1 las regiones oscuras se volverán más brillantes y el
    histograma se moverá a la derecha, mientras que con un gamma > 1, esto
    será lo opuesto
    
    La corrección gamma tiende a añadir menos efecto de saturación ya que el
    mapeo es no lñineal y no hay saturación numérica, como en otros métodos
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Apertura de la imagen
img = cv2.imread('endgame.jpeg')
# Abrir una ventana con la imagen
cv2.imshow('image',img)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

# Histograma imagen original
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist_full)
plt.title("Histograma imagen original")
plt.show()

# Corrección gamma
gamma = 0.4
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

res = cv2.LUT(img, lookUpTable)

cv2.imshow('correccion',res)
# Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

# Histograma imagen corregida
hist_full2 = cv2.calcHist([res],[0],None,[256],[0,256])
plt.plot(hist_full2)
plt.title("Histograma imagen corregida")
plt.show()

cv2.destroyAllWindows()