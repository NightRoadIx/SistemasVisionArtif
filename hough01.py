'''
	La transformada de Hough es un método que es utilizado para la detección de 
	cualquier forma, si esa forma puede ser representada por medio de una función
	matemática, puede detectar esa forma, a pesar de que este rota o distorsionada.
	
	Por ejemplo, una línea puede ser representada por medio de la siguiente ecuación:
	y = mx + c o de forma paramétrica r = x cos(theta) + y sen(theta)
	donde r es la distancia perpendicualr del origen a la línea y theta es el ángulo
	formado por la línea perpendicular y el eje horizontal medido en sentido horario
	(esto es arbitrario, pero así es representado en OpenCV).
	
	Ahora para que funcione el método por medio de la trasnformada de Hough se realizan
	los siguientes pasos:
	1.- Crear un arreglo 2D o acumulador (para almacenar los valores de dos parámetros)
	    y se hacen cero.
	2.-Las filas representarán r y las columnas theta del arreglo anterior
	3.-El tamaño del arreglo dependerá de la precisión que se requiere. Por ejemplo, se 
	   puede suponer que si se requieren ángulos de 1° de precisión, se tendrán 180 columnas
	4.-Para r, la máxima distancia posible es la longitud de la longitud de la diagonal de la imagen.
	   Por lo que al tomar un pixel de precisión, el número de columnas puede ser la longitud diaginal
	   de la imagen
'''
import cv2
import numpy as np

# Se hara la lectura de la imagen
img = cv2.imread('left04.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

# Se convierte a nivel de grises
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', gray)
cv2.waitKey(0)

# Después se le aplica la detección de bordes por Canny 
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('Bordes', edges)
cv2.waitKey(0)
# En este punto es recomdnable en ocasiones realizar primero
# un filtrado, después un la detección de bordes, para 
# posteriormente hacer erosión y ensanchamiento

# La función HpughLines permitirá obtener el arreglo 2D requerido
# en la transformada de Hough
# Parámetros (en orden):
# imagen a la que se le aplicará la transformación
# La resolución de la distancia para el acumulador (r)
# La resolución en ángulo para el acumulador (theta)
# umbral para conocer si se toma como línea o no (revisar: https://www.learnopencv.com/hough-transform-with-opencv-c-python/)
# posterioemente se incluye un None, estuve revisando por varios lados y no comprendo por que razón se debe incluir
# este parámetro, ya que en caso contrario, el programa falla
lines = cv2.HoughLines(edges,1,np.pi/180,150,None)

# en ocasiones (sobre todo si no se coloca None) la transformada regresa un valor None y todo falla
if lines is not None:
    # Recorrer los resultados
    for i in range(0, len(lines)):
        # Obtener los valores de rho (distacia)
        rho = lines[i][0][0]
		# y de theta (ángulo)
        theta = lines[i][0][1]
		# guardar el valor del cos(theta)
        a = np.cos(theta)
		# guardar el valor del sen(theta)
        b = np.sin(theta)
		# guardar el valor de r cos(theta)
        x0 = a*rho
		# guardar el valor de r sen(theta), todo se está haciendo de forma paramétrica
        y0 = b*rho
		# Ahora todo se recorrerá de -1000 a 1000 pixeles
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        
		# Mostrar los valores hallados
        print("({},{})  ({},{})".format(x1,y1, x2,y2))
		# Generar las líneas para montarlas en la imagen original
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# Mostrar la imagen original con todas las líneas halladas
cv2.imshow('Asia', img)
cv2.waitKey(0)