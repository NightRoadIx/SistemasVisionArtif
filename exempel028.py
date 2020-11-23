'''
	DETECCIÓN DE ESQUINAS DE HARRIS
	Las esquinas son regiones de una imagen con una gran variabilidad en intensidad
	en todas las direcciones. En 1988, Chris Harris y Mike Stephens presentaron
	un algoritmo en el artículo "A combined Corner and Edge Detector".
	Simplemente lo que realiza es encontrar la diferencia en la intensidad para
	un desplzamiento de (u,v) en todas las direcciones.
	El artículo esta disponible en:
	https://www.semanticscholar.org/paper/A-Combined-Corner-and-Edge-Detector-Harris-Stephens/6818668fb895d95861a2eb9673ddc3a41e27b3b3
	
'''
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
# Se manda a llamar una imagen con bordes como un tablero de ajedrez
img = cv2.imread("sudokusmall.jpg")
# Cambiamos a escala de grises
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Aquí se hace la modificación de la imagen uint8 a tipo flotante
# pues el algoritmo así lo requiere
gray = np.float32(gray)
# Se aplica la detección de esquinas de Harris, la cual requiere:
# la imagen en escala de grises de tipo flotante
# tamaño del vecindario que se considerará para la detección (nxn)
# Parámetro de apertura del filtro derivativo de Sobel
# Parámetro libre del detector de Harris (k en la ecuación R = Det(M) - k(Tr(M))^2)
dst = cv2.cornerHarris(gray,2,3,0.04)

# La imagen resultante es dilatada
dst = cv2.dilate(dst,None)

# Se aplica un unmbral para un valor óptimo, varia de acuerdo a cada imagen
img[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows() 
