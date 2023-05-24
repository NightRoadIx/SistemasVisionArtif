from imutils import paths
import numpy as np
import imutils
import cv2
import matplotlib.pyplot as mp

def find_stickynote(image):
    # Convertir la imagen a escala de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Hacerla borrosa
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # Detectar los bordes
    edged = cv2.Canny(gray, 35, 125)
    # Encontrar los contornos en la imagen de bordes y mantener
    # el más largo, asumiendo que será la pieza de papel en la misma imagen
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key = cv2.contourArea)
    M = cv2.moments(c)
    # Calcular la caja que rodea al objeto y regresarlo
    return cv2.minAreaRect(c), [int(M["m10"] / M["m00"]),int(M["m01"] / M["m00"])]

# Se aplicará el principio de similaridad de triángulos
# Supongamos un objeto con ancho W y a una distancia D de la cámara
# al tomar una fotografía se mide el ancho aparente en pixeles P
# lo cual nos permite obtener la distancia focal de la cámara F
# F = (P x D) / W
def distance_to_camera(knownWidth, focalLength, perWidth):
    # Calcular y regresar la distancia del marcador a la cámara
    return (knownWidth * focalLength) / perWidth

# Iniciar las distancias conocidas de la cámara al objeto
KNOWN_DISTANCE = 30
# Iniciar el ancho del objeto conocido
KNOWN_WIDTH = 5

# Cargar la imagen que contiene el objeto con el ancho conocido para conocer la distancia focal
image = cv2.imread("imagen.jpg")
sticky_note, centre = find_stickynote(image)
focalLength = (sticky_note[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
dist = distance_to_camera(KNOWN_WIDTH, focalLength, sticky_note[1][0])
# Dibujar una caja alrededor de la imagen y desplegarla
box = cv2.cv.BoxPoints(sticky_note) if imutils.is_cv2() else cv2.boxPoints(sticky_note)
box = np.int0(box)
mp.figure(figsize=(15,15))
mp.plot([centre[0],box[1][0]-100],[centre[1],box[1][1]-50],color="yellow", linewidth=3)
mp.plot([box[1][0],box[2][0]],[box[1][1],box[2][1]],color="white", linewidth=3)
mp.plot([box[2][0],box[3][0]],[box[2][1],box[3][1]],color="white", linewidth=3)
mp.plot([box[3][0],box[0][0]],[box[3][1],box[0][1]],color="white", linewidth=3)
mp.plot([box[0][0],box[1][0]],[box[0][1],box[1][1]],color="white", linewidth=3)
mp.text(box[1][0]-160, box[1][1]-60, "{} cm".format(str(dist)), color="orange", fontdict={"fontsize":20,"fontweight":'bold'})
mp.imshow(image)
mp.show()
