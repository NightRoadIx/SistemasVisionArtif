import cv2
import numpy as np
import matplotlib.pyplot as mp
import imutils
from imutils import contours
from imutils import perspective
from scipy.spatial import distance as dist
import imageio

# Lista vacía para guardar las imágenes
imagenes = []
# Velocidad del gif
fps = 1

# Relación píxeles - distancia
# EN ESTE CASO SE SUPONE UNA RELACIÓN 1 PX - 1 CM
ppMx, ppMy = 1, 1

def puntoMedio(ptA, ptB):
    """
    Determina el punto medio entre 2 puntos
    unidos por una recta
    :param ptA: Punto inicial (x, y)
    :param ptB: Punto final (x, y)
    :return: La posición (x, y) del punto medio
    """
    return ( (ptA[0] + ptB[0]) * 0.5  , (ptA[1] + ptB[1]) * 0.5 )

# Capturar la imagen a analizar
img = cv2.imread("figuras.png")
# Cambiar espacio de color
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Preprocesamiento con un filtro Guassiano
filtro = cv2.GaussianBlur(gris, (7, 7), 0)
# Umbralizar la imagen
ret, umbral = cv2.threshold(filtro,
                            70, 255,
                            cv2.THRESH_BINARY)
# Encontrar los contornos
# lo cual regresa una tupla (contornos, jerarquía)
cnts = cv2.findContours(
    umbral, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
# Extraer los contornos localizados
cnts2 = imutils.grab_contours(cnts)
#  Acomodar los contornos de izquierda a derecha
# para comenzar a calibrar
(cnts3, _) = contours.sort_contours(cnts2)

# Recorrer los contornos individualmente
for c in cnts3:
    if(cv2.contourArea(c) < 10):
        continue

    # Obtener una imagen copia de la original
    imgCopia = img.copy()

    # Calcular la caja rotada fuera del contorno
    # Primeramente, se ajusta un rectángulo
    # rotado alrededor de un conjunto de
    # puntos en un plano 2D; el rectángulo tiene
    # la propiedad de tener el área mínima entre
    # todos los rectángulos posibles que pueden
    # ser colocados alrededor del conjunto de puntos
    caja = cv2.minAreaRect(c)
    # Luego se obtienen las coordenadas de los
    # vértices de un rectángulo rotado
    caja = cv2.boxPoints(caja)
    # Convertir a un arreglo tipo numpy de enteros
    caja = np.array(caja, dtype="int")

    # Ordenar los puntos en el contorno para
    # que aparezcan de superior izquierda a
    # superior derecha, luego a
    # inferior derecha y termina inferior izquierda
    caja = perspective.order_points(caja)
    cv2.drawContours(imgCopia, [caja.astype("int")],
                     -1, (0, 255, 0), 2)

    # Recorrer las esquinas de las cajas y dibujarlos
    for (x, y) in caja:
        cv2.circle(imgCopia, (int(x), int(y)), 5, (0, 0, 255), -1)

    # Calcular el punto medio
    # Desempaquetar la caja calculada en orden
    (si, sd, id, ii) = caja
    (sisdX, sisdY) = puntoMedio(si, sd)
    (iiidX, iiidY) = puntoMedio(ii, id)

    (siiiX, siiiY) = puntoMedio(si, ii)
    (sdidX, sdidY) = puntoMedio(sd, id)

    # Dibujar los puntos medios
    cv2.circle(imgCopia, (int(sisdX), int(sisdY)), 5, (255, 0, 0), -1)
    cv2.circle(imgCopia, (int(iiidX), int(iiidY)), 5, (255, 0, 0), -1)
    cv2.circle(imgCopia, (int(siiiX), int(siiiY)), 5, (255, 0, 0), -1)
    cv2.circle(imgCopia, (int(sdidX), int(sdidY)), 5, (255, 0, 0), -1)
    # Dibujar líneas entre los puntos
    cv2.line(imgCopia, (int(sisdX), int(sisdY)),
             (int(iiidX), int(iiidY)), (255,0,255), 2)
    cv2.line(imgCopia, (int(siiiX), int(siiiY)),
             (int(sdidX), int(sdidY)), (255,0,255), 2)

    # Calcular las distancias en píxeles (A para eje y, B para eje x)
    dA = dist.euclidean((sisdX, sisdY), (iiidX, iiidY))
    dB = dist.euclidean((siiiX, siiiY), (sdidX, sdidY))

    # convertir a cm usando la relación
    # de pixeles a métrica o unidad de distancia (ppM)
    dimA = dA / ppMy
    dimB = dB / ppMx

    # Colocar las dimensiones localizadas
    # suponiendo cm
    cv2.putText(imgCopia, "{:.1f}cm".format(dimA),
                (int(sisdX - 15), int(sisdY - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                (255, 255, 255), 2
                )
    cv2.putText(imgCopia, "{:.1f}cm".format(dimB),
                (int(sdidX + 10), int(sdidY)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                (255, 255, 255), 2
                )

    # Mostrar las imágenes de los tamaños de
    # los objetos localizados
    cv2.imshow("Final", imgCopia)
    cv2.waitKey(0)
    # Ir guardando cada imagen
    imagenes.append(imgCopia)

# Salvar las imágenes en un gif animado
imageio.mimsave("dimensions.gif", imagenes, duration=1/fps)
cv2.destroyAllWindows()
