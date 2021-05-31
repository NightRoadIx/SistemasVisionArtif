import cv2
import pytesseract

# Se requiere descargar tesseract desde el sitio:
# https://github.com/UB-Mannheim/tesseract/wiki
# posteriormente instalar para python pytesseract
# pip install pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

placa = []

image = cv2.imread('auto001.jpg')
'''cv2.imshow('Original', image)
cv2.waitKey(0)'''

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
'''cv2.imshow('Gris', gray)
cv2.waitKey(0)'''

gray = cv2.blur(gray,(3,3))
'''cv2.imshow('GrayBlur', gray)
cv2.waitKey(0)'''

# Aquí ver la forma de automatizar los intervalos de Canny
canny = cv2.Canny(gray,150,200)
'''cv2.imshow('GrayCanny', canny)
cv2.waitKey(0)'''

canny = cv2.dilate(canny,None,iterations=1)
'''cv2.imshow('GrayCannyDilate', canny)
cv2.waitKey(0)'''


# Encontrar contornos
cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
'''cv2.drawContours(image,cnts,-1,(0,255,0),2)
cv2.imshow('OriginalContornos', image)
cv2.waitKey(0)'''

# Determinar las áreas de los contornos
for c in cnts:
    area = cv2.contourArea(c)
    # Detectar el rectángulo de la placa
    # obtener los puntos que roderan a cada contorno
    x,y,w,h = cv2.boundingRect(c)
    epsilon = 0.09*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)

    # Discriminando contornos y obteniendo el aspect ratio
    # También aquí se debe calcular el valor del área
    if len(approx) == 4 and area > 9000:
        print('area = ', area)
        #cv2.drawContours(image, [approx], 0, (0,255,0), 3)
        #cv2.imshow('OriginalPlacaContorno', image)
        
		# Aquí hay que determinar el aspect ratio de la placa
        aspect_ratio = float(w)/h
        if aspect_ratio > 2.4:
            placa = gray[y:y+h, x:x+w]
			# Leer el texto con pytesseract, utilizando la configuración
			# psm 11
			# Hay 13 modos de segmentación de página soportados
            text = pytesseract.image_to_string(placa, config='--psm 11')
            print('PLACA: ', text)
            
			# Mostrar la placa
            cv2.imshow('PLACA', placa)
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(image, text, (x-20, y-10), 1,2.2,(0, 255, 0), 3)        

# Mostrar la imagen final con la placa y el texto leído
cv2.imshow('Final', image)    
cv2.waitKey(0)
cv2.destroyAllWindows()