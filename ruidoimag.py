import numpy as np
import cv2
import random

# Función para añadir ruido sal y pimienta a una imagen
def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

cap = cv2.VideoCapture(0)

while(True):
    # Capturar cuadro por cuadro
    ret, frame = cap.read()

    # --Las operaciones que se hacen en el frame--
    # En este caso se hace que lo capturado este en escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    noise_img = sp_noise(gray,0.05)
    
    # Mostrar el frame resultante
    cv2.imshow('frame',noise_img)
    # La salida es mediante la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Una vez hecho todo, se tiene que liberar la captura de datos
cap.release()
cv2.destroyAllWindows()