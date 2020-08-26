import numpy as np
import cv2

# Mandar a llamar los clasificadores que trae Python para caras
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Y este es para ojos
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Aquí vamos leer una imagen cualquiera
img = cv2.imread('J:/13.jpg')
# Se convierte la imagen a gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aquí se van a almacenar la detección de caras con multiples escalas
# Todo esto se aplica en escala de grises para un cálculo más rápido
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# Para cada una de las siguientes características en la variable faces
for (x,y,w,h) in faces:
	# Se coloca un rectángulo azul donde detecta la cara
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
	# Se añade la detección de ojos para cada una de las áreas en donde se
	# realizó la detección del rostro
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
		# Se coloca un rectángulo verde
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
