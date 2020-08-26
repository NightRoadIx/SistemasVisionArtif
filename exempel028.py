import cv2
import numpy as np

# Obtener la captura del video del dispositivo 0
cap = cv2.VideoCapture(0)

while(1):

    # Captura cada cuadro
    ret, frame = cap.read()

    # Convertir de espacio de color BGR a HSV (esto permite identificar mejor la piel humana)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el intervalo del color rojo en HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([30,255,255])

    # Definir el intervalo del color verde en HSV
    lower_green = np.array([60,50,50])
    upper_green = np.array([90,255,255])

    # Definir el intervalo del color azul en HSV
    lower_blue = np.array([130,50,50])
    upper_blue = np.array([150,255,255])

    # Definir el intervalo del color violeta en HSV
    lower_violet = np.array([150,50,50])
    upper_violet = np.array([200,255,255])
	# RECORDAR QUE HSV REPRESENTA EL MATIZ, LA SATURACIÓN Y EL VALOR POR EL CONO DE COLOR

    # Umbralizar la imagen HSV para que solo se obtengan los colores azules
	# Esto genera una especie de "máscara" con los valores de los colores
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask4 = cv2.inRange(hsv, lower_violet, upper_violet)

    # Aplicar la máscara a la imagen original
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res2 = cv2.bitwise_and(frame,frame, mask= mask2)
    res3 = cv2.bitwise_and(frame,frame, mask= mask3)
    res4 = cv2.bitwise_and(frame,frame, mask= mask4)

    # Observar el resultado de la aplicación de las máscaras
    cv2.imshow('frame',frame)
	#cv2.imshow('hsv',hsv)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',mask)
    cv2.imshow('res2',mask2)
    cv2.imshow('res3',mask3)
    cv2.imshow('res4',mask4)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()