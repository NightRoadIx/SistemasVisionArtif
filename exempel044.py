import cv2

image = cv2.imread('figurasColores.png')
cv2.imshow('Original', image)
cv2.waitKey(0)
# Se convierte la imagen en escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', gray)
cv2.waitKey(0)
# Se aplica la detección de bordes mediante Canny
# esto nos dará una imagen binaria
canny = cv2.Canny(gray, 10, 150)
cv2.imshow('FiltroCanny', canny)
cv2.waitKey(0)
# Se aplica dilatación y erosión para mejorar la imagen
canny = cv2.dilate(canny, None, iterations=1)
cv2.imshow('Dilatar', canny)
cv2.waitKey(0)
canny = cv2.erode(canny, None, iterations=1)
cv2.imshow('Erosionar', canny)
cv2.waitKey(0)

# Encontrar los contornos de la imagen (con las opciones usadas se puede
# localizar los contornos externos)
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Dibujar los contornos sobre la imagen original
cv2.drawContours(image, cnts, -1, (0,255,0), 2)

cv2.destroyAllWindows()

#%%

# A partir de aquí se analizan cada uno de los contornos localizados
for c in cnts:
    
    # Este es el parámetro que especifica la precisión de la aproximación
    # Esta es la máxima distancia entre la curva original y su aproximación
    # con arcLength() se calcula el perímetro del contorno o la longitud de
    # la curva (True/False, indica si la curva es cerrada o no)
    # Esto se tiene que multiplicar por un porcentaje
    epsilon = 0.01*cv2.arcLength(c,True)
    # Aquí también se toma en cuenta si la curva es cerrada o no
    # La función utiliza el algoritmo Ramer-Douglas-Peucker
    # el algoritmo diezma una curva compuesta por segmentos de línea a una 
    # curva similar con menos puntos
    approx = cv2.approxPolyDP(c,epsilon,True)
    #print(len(approx))
    # Con esto se obtienen los puntos (x,y) & el ancho, alto del contorno
    x,y,w,h = cv2.boundingRect(approx)
    
    # La variable approx da información del tipo de figura
    # tiene algo que ver con la cantidad de lados de la misma
    if len(approx)==3:
        cv2.putText(image,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
        
    # Para diferenciar si es un cuadrado o rectángulo
    if len(approx)==4:
        # Se toma en cuenta el aspect_ratio = ancho / alto
        aspect_ratio = float(w)/h
        print('aspect_ratio= ', aspect_ratio)
        
        if aspect_ratio == 1:
            cv2.putText(image,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        else:
            cv2.putText(image,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
    
    if len(approx)==5:
        cv2.putText(image,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)

    if len(approx)==6:
        cv2.putText(image,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)

    if len(approx)>10:
        cv2.putText(image,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
        
    # Dibujar los contornos
    cv2.drawContours(image, [approx], 0, (0,255,0),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)

cv2.destroyAllWindows()