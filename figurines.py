# La de procesamiento de imagenizaniosización
import cv2
import numpy as np
import matplotlib.pyplot as mp

def detectar(c):
    '''
    Función para determinar
    :param c: contorno de entrada o secuencia de puntos que forman una línea abierta o cerrada
    :return:
    '''
    # Obtener el perimetro de la figura
    perico = cv2.arcLength(c, True)
    # Luego se aplica la función approxPolyDP()
    # la cual simplifica contornos poligonales al reducir el
    # número de vértices, pero manteniendo la forma general del contorno
    # Parámetros: (conjunto de puntos del contorno, parámetro precisión que controla la
    # distancia máxima entre el original y la aproximación, bool que especifica si es un
    # contorno cerrado o no)
    approx = cv2.approxPolyDP(
      c, 0.04 * perico, True
    )
    return approx

# PASOS DEL PROCESAMIENTO DE IMÁGENES
# "Ler" la imagen
img = cv2.imread("figuras.png")
# Copiar la imagen
imgCopia = img.copy()

# Cambiar a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hagamos la imagen bien borrosa
filtro = cv2.GaussianBlur(gris, (5,5), 0)

# Luego, se le aplica un umbralizado
ret, umbral = cv2.threshold(filtro,
                          65, 255,
                          cv2.THRESH_BINARY)
print(f"Valor umbral: {ret}")

# Aplicamos un detector de contornos
cnts, _ = cv2.findContours(
    umbral, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
print(f"Localizados {len(cnts)} contornos")

# Dibujar los contornos
cv2.drawContours(
    imgCopia,
    cnts,
    -1,
    (0,255,0), 4
    )

# Recorrer todos los contornos
for c in cnts:
    # Obtener los momentos de la imagen
    # https://learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
    # https://www.pythonpool.com/opencv-moments/
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # Dibujar centroides
    cv2.circle(imgCopia, (cX, cY), 5, (0,0,0), -1)
    print("Lados: ", len(detectar(c)))

cv2.imshow("Final", imgCopia)
cv2.waitKey(0)

cv2.destroyAllWindows()
