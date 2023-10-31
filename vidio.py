import cv2
import numpy as np
import matplotlib.pyplot as mp

# Crear el objeto que maneja videos
# un número representa el dispositivo a usar (cámara)
# el nombre de un archivo, el posible video
cap = cv2.VideoCapture('Checo.mp4')

# Obtener la velocidad de los fotogramas
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS: ", fps)
# El tamaño del video
fWidth = int(cap.get(3))
fHeight = int(cap.get(4))
tam = (fWidth, fHeight)
print("Tamaño: ", tam)

# Genera un objeto para guardar el video
resultado = cv2.VideoWriter(
    'nuevo.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    30, tam
)

# Kernel para detección de puntos
kernel2 = np.array(
    [[-1,-1,-1],
     [-1,8,-1],
     [-1,-1,-1]]
)

while True:
    # Leer el dispositivo de entrada
    ret, frame = cap.read()
    # Si ret es False, quiere decir que no se
    # obtuvo información alguna
    if ret == False:
        break  # Entonces, se rompe y no hace nada

    # # # # # # # # # # # # # # # # # # # # 
    # Continúa la lógica del programa
    # Tamaño del video
    height, width, _ = frame.shape
    # Pasar a espacio de color HSV
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Aplicar un filtro detector de puntos en espacio HSV
    laBarata = cv2.filter2D(imgHSV, -1, kernel2)
    # Guardar
    resultado.write(laBarata)
    # Mostrar
    cv2.imshow("Vidio", laBarata)
    # # # # # # # # # # # # # # # # # # #

    # Sí se presiona una tecla, en este caso ESC
    # sale del ciclo
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Una vez hecho todo, liberar a Willy
# El video
cap.release()
# El archivo guardado
resultado.release()
# Cerrar todas las ventanas
cv2.destroyAllWindows()

