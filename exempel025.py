import cv2
import sys

# Mandar a llamar los clasificadores ya entrenados
# En este caso, los archivos con los clasificadores se colocaron en la ruta:
# C:\opencv\build\etc\haarcascades\
faceCascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_alt2.xml')
# Y este es para ojos
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')
# Y este es para la sonrisa
smile_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_smile.xml')

# Iniciar con la captura de video
video_capture = cv2.VideoCapture(0)

# Realizar todo en un ciclo infinito
while True:
    # Se captura cuadro a cuadro
    ret, frame = video_capture.read()
	
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ecualizar la imagen para una mejora en la deteccion
    # cv2.equalizeHist(gray,gray);

    # En este paso se van a almacenar la detección de caras con multiples escalas
    faces = faceCascade.detectMultiScale(
        gray,				# Esto se hace en escala de grises para mayor velocidad
        scaleFactor=1.1,		# En caso de que existan rostros lejanos, se compensa mediante esto
        minNeighbors=5,			# Aquí se define cuantos objetos han sido detectados
        minSize=(20, 20)		# Se define el tamaño mínimo de la ventan
    )

    # Dibujar un rectángulo alrededor de la cara
    # sobre los elementos del rostro
    for (x, y, w, h) in faces:
        # Estos valores nos dan la posición del rostro x,y,w,h
	# Con un color BRG
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=2,
            minSize=(20, 20)
        )
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,200,255),2)

        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=1,
            minSize=(30, 30)
        )
        for (ex,ey,ew,eh) in smile:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(150,20,0),2)            

    # Mostrar el frame resultante
    cv2.imshow('Video', frame)

    # Mientras no se presione la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Una vez que re realiza todo, hay que liberar la captura de video y destruir ventanas
video_capture.release()
cv2.destroyAllWindows()
