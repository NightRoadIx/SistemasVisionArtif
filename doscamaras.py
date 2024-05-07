import cv2
import numpy as np
import matplotlib.pyplot as mp

print("Versión: " + cv2.__version__)

# Leer un video
#cap = cv2.VideoCapture(
#    r'C:\Users\s_bio\OneDrive\Documentos\conda\clanTreviAndrade\Checo.mp4'
#)
# Observar 2 cámaras
cap0 = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)

# Obtener la velocidad de los fotogramas
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS: ", fps)
# El tamaño del video
fWidth = int(cap.get(3))
fHeight = int(cap.get(4))
tam = (fWidth, fHeight)
print("Tamaño: ", tam)

# Kernel para detección de puntos
kernel2 = np.array(
    [[-1,-1,-1],
     [-1,8,-1],
     [-1,-1,-1]]
)

# Recorrer el video cuadro a cuadro
while True:
    # Leer el dispositivo de entrada
    ret, frame = cap.read()
    ret0, frame0 = cap0.read()
    if ret == False:
        break
    # PROCESAR
    # Pasar a HSV
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    laBarata = cv2.filter2D(imgHSV, -1, kernel2)
    frame0 = cv2.GaussianBlur(frame0, (5,5), -1)
    # Mostrar la imagen
    h0, w0, _ = frame0.shape
    h1, w1, _ = frame.shape
    frame3 = cv2.hconcat([frame0, frame])
    cv2.imshow("Vidio", frame3)

    # Si se presiona la tecla ESC sale del ciclo
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Y luego se libera a Willy
cap.release()
# Y se cierra la ventana
cv2.destroyAllWindows()












