import cv2
import numpy as np

rojoBajo1 = np.array([0, 140, 90], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 140, 90], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
    imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    maskRojo1 = cv2.inRange(imageHSV, rojoBajo1, rojoAlto1)
    maskRojo2 = cv2.inRange(imageHSV, rojoBajo2, rojoAlto2)
    mask = cv2.add(maskRojo1,maskRojo2)
    mask = cv2.medianBlur(mask, 7)
    
    redDetected = cv2.bitwise_and(frame,frame,mask=mask)
    invMask = cv2.bitwise_not(mask)
    bgGray = cv2.bitwise_and(imageGray,imageGray,mask=invMask)
    finalImage = cv2.add(bgGray,redDetected)
    
    cv2.imshow('Resultado', finalImage)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
# Leer la imagen
image = cv2.imread('trapeador.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Pasamos las imágenes de BGR a: GRAY (esta a BGR nuevamente) y a HSV
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', imageGray)
cv2.waitKey(0)
# Con esto se logra tener una imagen de 3 canales mostrando niveles de gris
imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
cv2.imshow('Gris3Canales', imageGray)
cv2.waitKey(0)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', imageHSV)
cv2.waitKey(0)

# Detectamos el color rojo en 2 niveles
maskRojo1 = cv2.inRange(imageHSV, rojoBajo1, rojoAlto1)
cv2.imshow('MascaraRojo1', maskRojo1)
cv2.waitKey(0)
maskRojo2 = cv2.inRange(imageHSV, rojoBajo2, rojoAlto2)
cv2.imshow('MascaraRojo2', maskRojo2)
cv2.waitKey(0)
# Se realiza la suma de ambas máscaras en rojo
mask = cv2.add(maskRojo1,maskRojo2)
cv2.imshow('MascarasRojo', mask)
cv2.waitKey(0)
# Se aplica un filtro para mejorar los bordes
mask = cv2.medianBlur(mask, 7)
cv2.imshow('MascarasRojoFiltro', mask)
cv2.waitKey(0)

# Con esto se puede observar la máscara en el color original BGR
redDetected = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('RojoMascara', redDetected)
cv2.waitKey(0)

# Fondo en grises
invMask = cv2.bitwise_not(mask)
cv2.imshow('FondoGrises', invMask)
cv2.waitKey(0)

# Aquí en el área en blanco se mostrará la imagen en grises
bgGray = cv2.bitwise_and(imageGray,imageGray,mask=invMask)
cv2.imshow('GrisMascaraNegro', bgGray)
cv2.waitKey(0)

# Se suma bgGray + redDetected para obtener la imagen final en gris resaltando
# el rojo
finalImage = cv2.add(bgGray,redDetected)
cv2.imshow('finalImage', finalImage)
cv2.waitKey(0)

cv2.destroyAllWindows()
'''
