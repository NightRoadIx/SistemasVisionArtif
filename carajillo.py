import cv2
import numpy as np
import matplotlib.pyplot as mp
import math

def distancia(pA, pB):
    """
    Función para el cálculo de la distancia entre 2 puntos pA, pB
    :param pA: Punto inicial
    :param pB: Punto final
    :return: El valor de la distancia en píxeles entre el pA y pB
    """
    return math.sqrt((pA[0]-pB[0])**2 + (pA[1]-pB[1])**2)

def filtroIdealPB(D0, tam):
    """
    Imagen de un filtro pasabajas con frecuencia de corte D0 y tamaño tam
    :param D0: Frecuencia de corte
    :param tam: Tamaño de la imagen a generar
    :return: Imagen de un filtro pasabajas
    """
    base = np.zeros(tam[:2])
    fil, col = tam[:2]
    centro = (fil/2, col/2)
    for x in range(col):
        for y in range(fil):
            if distancia((y, x), centro) < D0:
                base[y, x] = 1
    return base

def filtroGaussPB(D0, tam):
    """
    Imagen de un filtro pasabajas gaussiano con frecuencia de corte D0 y tamaño tam
    :param D0: Frecuencia de corte
    :param tam: Tamaño de la imagen a generar
    :return: Imagen de un filtro pasabajas
    """
    base = np.zeros(tam[:2])
    fil, col = tam[:2]
    centro = (fil/2, col/2)
    for x in range(col):
        for y in range(fil):
            base[y, x] = math.exp(((-distancia((y,x),centro)**2)/(2*(D0**2))))
    return base

def filtroIdealPA(D0, tam):
    """
    Imagen de un filtro pasaltas con frecuencia de corte D0 y tamaño tam
    :param D0: Frecuencia de corte
    :param tam: Tamaño de la imagen a generar
    :return: Imagen de un filtro pasabajas
    """
    base = np.ones(tam[:2])
    fil, col = tam[:2]
    centro = (fil/2, col/2)
    for x in range(col):
        for y in range(fil):
            if distancia((y, x), centro) < D0:
                base[y, x] = 0
    return base

def filtroGaussPA(D0, tam):
    """
    Imagen de un filtro pasaltas gaussiano con frecuencia de corte D0 y tamaño tam
    :param D0: Frecuencia de corte
    :param tam: Tamaño de la imagen a generar
    :return: Imagen de un filtro pasabajas
    """
    base = np.zeros(tam[:2])
    fil, col = tam[:2]
    centro = (fil/2, col/2)
    for x in range(col):
        for y in range(fil):
            base[y, x] = 1 - math.exp(((-distancia((y,x),centro)**2)/(2*(D0**2))))
    return base

# Frecuencia de corte D0
D0 = 10

# ADQUISICIÓN DE IMÁGENES
# Leer la imagen
img = cv2.imread("gato.jpg")
# Cambiamos a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mp.subplot(3,3,1)
mp.imshow(gris, cmap='gray')
mp.title('Imagen original')
mp.xticks([]), mp.yticks([])

# TRANSFORMADA DE FOURIER
# Una imagen en escala de grises es una señal
# en 2D, cuya función f(x,y) representa el
# nivel de intensidad de cada uno de los píxeles
# por lo tanto, se puede aplicar la transformada
# de Fourier para obtener F(jw), la señal en
# en el espacio de Frecuencias
F = np.fft.fft2(gris)
# Se obtiene la magnitud de F(jw), ya que
# se trata de una función de variable compleja
# y no es posible graficar. Además, se grafica
# en una escala logarítmica para que se alcance
# a distinguir y así poder interpretar
# Esto genera valores en decibeles
M = 20*np.log(np.abs(F))
mp.subplot(3,3,2)
mp.imshow(M, cmap='gray')
mp.title('Fourier de original')
mp.xticks([]), mp.yticks([])

# Posteriormente, se modifica el espectro para mover
# la frecuencia 0 al centro de la imagen
# Se obtiene la transformada recorrida
Fshift = np.fft.fftshift(F)
Mshift = 20*np.log(np.abs(Fshift))
mp.subplot(3,3,3)
mp.imshow(Mshift, cmap='gray')
mp.title('Fourier de original shifted')
mp.xticks([]), mp.yticks([])

# FILTRADO
# Generalmente, el filtrado se aplica con filtros
# pasa-altas o gaussianos para reducir el ruido de las
# imágenes, siendo estos filtros espaciales
# Para el caso de las imágenes, se requiere generar un
# filtro H(u,v) con forma de disco, usando pixeles B&W.
# El filtro ideal esta caracterizado por la ecuación:
# |H(u, v)| = 1 donde D(u,v) > D0
# |H(u, v)| = 0 donde D(u,v) < D0
# donde D0 es la frecuencia de corte; sin embargo, este
# filtro introduce artefactos en la imagen, los cuales se
# presentan como oscilaciones que aparecen cerca de los bordes
# de la imagen resultando en imágenes no naturales

# Filtro
H = filtroIdealPB(D0, gris.shape)
mp.subplot(3,3,6)
mp.imshow(np.abs(H), cmap='gray')
mp.title('Filtro fc=' + str(D0))
mp.xticks([]), mp.yticks([])

# Multiplicar el filtro y la imagen para obtener la imagen filtrada
# G(u,v) = F(u,v)H(u,v)
G = Fshift*H
GM = np.log(1+np.abs(G))
mp.subplot(3,3,9)
mp.imshow(GM, cmap='gray')
mp.title('Espectro imagen filtrada shifted')
mp.xticks([]), mp.yticks([])

# Recorrer la imagen filtrada en frecuencia
GH = np.fft.ifftshift(G)
GHM = np.log(1+np.abs(GH))
mp.subplot(3,3,8)
mp.imshow(GHM, cmap='gray')
mp.title('Espectro imagen filtrada')
mp.xticks([]), mp.yticks([])

# Obtener la transformada inversa de Fourier
g = np.fft.ifft2(GH)
gm = np.log(20*np.abs(g))
mp.subplot(3,3,7)
mp.imshow(gm, cmap='gray')
mp.title('Imagen filtrada')
mp.xticks([]), mp.yticks([])
mp.show()

cv2.destroyAllWindows()
