import numpy as np
import random
import math

def sp_noise(image,prob):
    """
    Función para añadir ruido sal y pimienta a una imagen
    :param image: Imagen a mostrar
    :param prob: Valor de la fdp del ruido
    :return: La imagen corrompida con ruido sal y pimienta
    """
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def zone(x, y):
    """
    Función para calcular (1/2) * (1 + cos(x^2 + y^2))
    :param x: valor del punto en x
    :param y: valor del punto en t
    :return: el valor calculado
    """
    return 0.5 * (1 + math.cos(x * x + y * y))

# Localizar el centro de la imagen
def dist_center(y, x, SIZE):
    """
    Función para localizar la distancia del centro de una imagen a un punto (x,y)
    :param y: Valor en y del punto a medir
    :param x: Valor en x del punto a medir
    :return: La distancia euclideana del centro al punto (x,y)
    """
    center = SIZE / 2
    return math.sqrt( (x - center)**2 + (y - center)**2)

def generarCirculos(SIZE = 597, start = -7.2, end = 8.2, step = 0.0275):
    """
    Función para generar una imagen de círculos concéntricos en escala de grises
    :param SIZE: Tamaño de la imagen (SIZE x SIZE)
    :param start: Valor donde inician los círculos
    :param end: Valor donde finalizan los círculos
    :param step: Pasos con los cuales se generan los círculos
    :return: La imagen con los círculos concéntricos
    """
    # Se crea una imagen con una sola capa (en escala de grises) a ceros
    image = np.zeros((SIZE, SIZE))
    # Generar la imagen
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            if dist_center(y, x, SIZE) > 300:
                continue
            y_val = start + y * step
            x_val = start + x * step
            image[y, x] = zone(x_val, y_val)

    # Realizar la transformación de float32 a uint8
    # La imagen esta normalizada
    image *= 255
    image = image.astype(np.uint8)
    return image
