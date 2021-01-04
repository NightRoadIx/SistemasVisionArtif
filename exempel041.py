import cv2
import numpy as np

# # # # # # # PARAMETROS # # # # # # #
# Imagen a cargar
filename =  "trapeador.jpg"

# Parámetros
blur_val = 5
linea = 11
k = 8

# # # # # # # APERTURA DE LA IMAGEN # # # # # # #
# Apertura de la imagen
img = cv2.imread(filename)

# Mostrar la imagen
cv2.imshow('Original', img)
cv2.waitKey(0)

# # # # # # # CREAR MÁSCARA DE CONTORNOS # # # # # # #
# Cambiar la imagen a nivel de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Mostrar la imagen
cv2.imshow('Escala de grises', gris)
cv2.waitKey(0)

# Colocar un filtro de mediana
gris_blur = cv2.medianBlur(gris, blur_val)
# Mostrar la imagen
cv2.imshow('Filtro de mediana', gris_blur)
cv2.waitKey(0)

# Encontrar los contornos
edges = cv2.adaptiveThreshold(gris_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, linea, blur_val)
# Mostrar la imagen
cv2.imshow('Contornos', edges)
cv2.waitKey(0)

# # # # # # # REDUCIR LA PALETA DE COLOR # # # # # # #
# Reestructurar la imagen para el algoritmo de K-Means
# En este caso se convierte en una matriz de números flotantes de 32 bits
# (así lo requiere el algoritmo) de [n, 3], donde cada columna representa
# las características a analizar (en este caso los niveles de color BGR)
# y "n" es el número total de pixeles
data = np.float32(img).reshape((-1,3))

# Determinar los criterios de finalización del algoritmo de K-Means
# (tipo, maximo_iteraciones, epsilon)
# cv.TERM_CRITERIA_EPS - detener el algoritmo cuando la precisión (exactitud) se alcance
# cv2.TERM_CRITERIA_MAX_ITER - detener tras un número máximo de iteraciones
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementar el algoritmo K-Means
# Este es un método de agrupamiento que permite generar k grupos a partir de
# N observaciones, en el que cada observación pertenece al grupo cuyo valor
# medio es el más cercano
# k representa el número de "clústers" o grupos requeridos
# después se coloca el número de intentos a realizar el algoritmo
# finalmente coloca la bandera de como se tomarán los centros iniciales
# Se obtienen:
# Que tan compacto es el grupo
# Las etiquetas que producen la compactación ideal de los grupos
# El valor central de cada uno de los grupos
ret, label, centro = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# Reconvertir los valores a enteros de 8 bits
centro = np.uint8(centro)
# Se genera un vector con los valores hallados
resultado = centro[label.flatten()]
# Se reestructura la matriz al tamaño de la imagen
resultado = resultado.reshape(img.shape)
# Mostrar la imagen
cv2.imshow('Paleta de color', resultado)
cv2.waitKey(0)

# Ajustar la imagen con un filtro bilateral
blurred = cv2.bilateralFilter(resultado, d=7, sigmaColor=200,sigmaSpace=200)
# Mostrar la imagen
cv2.imshow('Filtro Bilateral', blurred)
cv2.waitKey(0)

# # # # # # # COMBINAR IMAGEN COLOREADA CON MASCARA DE BORDES # # # # # # #
qfinal = cv2.bitwise_and(blurred, blurred, mask=edges)
# Mostrar la imagen
cv2.imshow('Final', qfinal)
cv2.waitKey(0)


# Eliminar todas las ventanas
cv2.destroyAllWindows()