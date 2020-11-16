import numpy as np
import cv2
 
# Cargamos la imagen
original = cv2.imread("monedas.jpg")
cv2.imshow("original", original)
cv2.waitKey(0)

# Convertimos a escala de grises
# se mandala imagen original y el espacio de color a utilizar
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
cv2.imshow("gris", gris)
cv2.waitKey(0) 

# Aplicar suavizado Gaussiano
# el último elemento representa la desviación estándar en el eje x, esto es la anchura de la campana
# de Gauss, con un 0, OpenCV calculará automáticamente el valor dependiendo de la máscara
# ver función cv2.getGaussianKernel(tamanno_apertura, sigma, ktype)
# sigma se calcula como 0.3*sigma((ksize-1)*0.5 - 1) + 0.8
# ktype, tipos de coeficientes
gauss = cv2.GaussianBlur(gris, (15,15), 0)
cv2.imshow("suavizado", gauss)
cv2.waitKey(0)

# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 50, 150)
cv2.imshow("canny", canny)
cv2.waitKey(0)

# Buscamos los contornos
# (Imagen binaria, modo_contorno, método aproximación)
# regresa una lista con los valores de los contornos
(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Mostramos el número de monedas por consola
print("He encontrado {} objetos".format(len(contornos)))

# Hallar contornos
# (imagen_oringinal, lista_de_contornos, numero_contornos, color_BGR, grosor_line_a_dibujar)
# numero_contornos si se pasa -1, pasa todos
cv2.drawContours(original,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", original)
cv2.waitKey(0)

cv2.destroyAllWindows()
