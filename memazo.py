import cv2
import numpy as np

# Abrir imagen 1
img1 = cv2.imread('colibri.jpg',-1)
# Abrir una ventana con la imagen
cv2.imshow('imagen1', img1)
# Esperar una tecla
cv2.waitKey(0)

# Obtener el tamaño de la imagen
cols, fils, _ = img1.shape

# Una línea
# cv2.line(imagen, punto inicial, punto final, colorBGR, pixeles)
img1C = cv2.line(img1, (0,0), (fils, cols), (0,0,255), 3)
img1C = cv2.line(img1, (fils,0), (0, cols), (0,0,255), 3)
# cv2.rectangle(imagen, puntoesqsupizq, puntoesqinfder, colorBGR, pixeles)
img1C = cv2.rectangle(img1, (int(fils/2-100), int(cols/2-100)), 
                      (int(fils/2+100), int(cols/2+100)), 
                      (0,0,255), 3)

img1C = cv2.circle(img1, (int(fils/2), int(cols/2)),
                   100, (0,255,0), 5) # -1

img1C = cv2.putText(img1, 'Memazo!', (10, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255),
                    2, cv2.LINE_AA)

# Abrir una ventana con la imagen
cv2.imshow('imagenMod', img1C)
# Esperar una tecla
cv2.waitKey(0)

print(img1C is img1)

cv2.destroyAllWindows()