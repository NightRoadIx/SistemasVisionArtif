import numpy as np
import cv2

# Marcar que se va a realizar la captura de video
cap = cv2.VideoCapture(0)

# Definir el codec (XVID) y crear el objeto VideoWriter
# Se prefiere el XVID sobre otros tipos
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# donde se muestra el video
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # Escribir el frame
        out.write(frame)

		# Mostrarlo también
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Liberar todo una vez que se haya terminado
cap.release()
out.release()
cv2.destroyAllWindows()