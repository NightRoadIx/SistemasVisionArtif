# Instalación de la librería Pandas para el manejo de grandes cantidades de datos estructurados
# pip install pandas
import cv2
import time
from datetime import datetime
import pandas

# Generar listas 
first_frame = None
status_list = [None, None]
times = []
# Crear una tabla de datos mediante la librería Pandas
df = pandas.DataFrame(columns=["Start", "End"])

# Iniciar con la captura de video
video = cv2.VideoCapture(0)

# Un ciclo infinito para la captura de fotogramas
while True:
 check, frame = video.read()
 status = 0
 
 # Cambiar a nivel de grises
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 # Aplicar un filtrado Gaussiano
 gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
 # Esto se activa cada que se trata del primer fotograma
 if first_frame is None:
  first_frame = gray
  continue
 
 # Obtener la diferencia absoluta con el primer fotograma
 delta_frame = cv2.absdiff(first_frame, gray)
 # Hacer un umbralizado binario
 thresh_delta = cv2.threshold(delta_frame, 150, 255, cv2.THRESH_BINARY)[1]
 # Dilatar la imagen
 thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
 # Encontrar los contornos de la imagen, se guardan en una especie de lista
 (_,cnts) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
 # Se hace un recorrido de los contornos
 for contour in cnts:
  # Si el área del contorno es menor a 500 pixeles
  # no realizar ninguna acción
  if cv2.contourArea(contour) < 500:
   continue
  status = 1
  # Generar un rectángulo alrededor del área del contorno
  (x, y, w, h) = cv2.boundingRect(contour)
  cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
 
 # Añadir cuantas veces se halla un contorno
 status_list.append(status)

 status_list = status_list[-2:]

 # Al verificar si se hallan los contornos
 # Verificar entonces la hora del sistema en ese momento
 if status_list[-1] == 1 and status_list[-2] == 0:
  times.append(datetime.now())
 if status_list[-1] == 0 and status_list[-2] == 1:
  times.append(datetime.now())
 
 print(status_list)
 print(times)
 #print(len(times))
 
 if len(times) > 1:
  for i in range(0, len(times), 2):
   #print(times[i])
   #print(times[i+1])
   df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)
 df.to_csv("Times.csv")
 
 cv2.imshow('frame', frame)
 cv2.imshow('Capturing', gray)
 cv2.imshow('Delta', delta_frame)
 cv2.imshow('Thresh', thresh_delta)
  
 if cv2.waitKey(1) & 0xFF == ord('q'):
  break;

video.release()
cv2.destroyAllWindows()
