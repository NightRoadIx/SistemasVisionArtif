import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capturar cuadro por cuadro
    ret, frame = cap.read()

    # --Las operaciones que se hacen en el frame--
    # En este caso se hace que lo capturado este en escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostrar el frame resultante
    cv2.imshow('frame',gray)
    # La salida es mediante la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Una vez hecho todo, se tiene que liberar la captura de datos
cap.release()
cv2.destroyAllWindows()
