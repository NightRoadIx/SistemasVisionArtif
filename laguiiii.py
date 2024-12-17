# Importar las librerías necesarias
from tkinter import *  # Librería para crear interfaces gráficas
from PIL import Image  # Para manejar imágenes
from PIL import ImageTk  # Para usar imágenes en la interfaz gráfica
import cv2  # Librería para procesamiento de video e imágenes
import imutils  # Librería para manipulación de imágenes y videos


# Función para iniciar la captura de video desde la cámara
def iniciar():
    """
    Inicia la captura de video desde la cámara y llama a la función visualizar
    para mostrar el video en la interfaz gráfica.
    """
    global cap, mostrar_hsv  # Declarar las variables globales
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Abrir la cámara (dispositivo 0) sin usar DirectShow (CAP_DSHOW)
    mostrar_hsv = False  # Inicializar el indicador para mostrar en espacio BGR
    visualizar()  # Llamar a la función visualizar para mostrar el video


# Función para mostrar el video en la interfaz gráfica
def visualizar():
    """
    Captura fotogramas de la cámara, los procesa y los muestra en la interfaz gráfica.
    La función es recursiva y se ejecuta periódicamente.
    """
    global cap, mostrar_hsv  # Declarar las variables globales
    if cap is not None:  # Verificar si la cámara está abierta
        ret, frame = cap.read()  # Leer un fotograma de la cámara
        if ret == True:  # Si el fotograma se obtuvo correctamente
            frame = imutils.resize(frame, width=640)  # Redimensionar el fotograma a un ancho de 640 píxeles

            # Cambiar el espacio de color según el indicador mostrar_hsv
            if mostrar_hsv:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertir a espacio HSV
            else:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir a espacio RGB (Tkinter lo requiere)

            # Convertir el fotograma en un objeto Image compatible con Tkinter
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            # Mostrar el fotograma en el label de la interfaz gráfica
            lblVideo.configure(image=img)
            lblVideo.image = img

            # Llamar a la función visualizar nuevamente después de 10 ms
            lblVideo.after(10, visualizar)
        else:  # Si no se obtuvo un fotograma, liberar la cámara
            lblVideo.image = ""  # Limpiar la imagen del label
            cap.release()  # Liberar la cámara


# Función para alternar entre los espacios de color BGR y HSV
def alternar_espacio_color():
    """
    Cambia el indicador mostrar_hsv para alternar entre los espacios de color
    BGR y HSV.
    """
    global mostrar_hsv  # Declarar la variable global
    mostrar_hsv = not mostrar_hsv  # Alternar el estado de mostrar_hsv


# Función para finalizar la captura de video
def finalizar():
    """
    Libera la cámara y detiene la captura de video.
    """
    global cap  # Declarar la variable cap como global
    cap.release()  # Liberar la cámara


# Declarar la variable global para la captura de video
cap = None
mostrar_hsv = False  # Variable para alternar entre BGR y HSV

# Crear la ventana principal de la interfaz gráfica
root = Tk()  # Inicializar el objeto root

# Crear el botón "Iniciar" y colocarlo en la ventana
btnIniciar = Button(root, text="Iniciar", width=45, command=iniciar)  # Botón que llama a la función iniciar
btnIniciar.grid(column=0, row=0, padx=5, pady=5)  # Ubicar el botón en la columna 0, fila 0 con márgenes

# Crear el botón "Finalizar" y colocarlo en la ventana
btnFinalizar = Button(root, text="Finalizar", width=45, command=finalizar)  # Botón que llama a la función finalizar
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)  # Ubicar el botón en la columna 1, fila 0 con márgenes

# Crear el botón para alternar entre BGR y HSV
btnAlternar = Button(root, text="Alternar espacio de color", width=45,
                     command=alternar_espacio_color)  # Botón que alterna entre espacios de color
btnAlternar.grid(column=0, row=1, columnspan=2, padx=5, pady=5)  # Ubicar el botón en la fila 1 y ocupar dos columnas

# Crear un label para mostrar el video en la ventana
lblVideo = Label(root)  # Label que mostrará los fotogramas capturados de la cámara
lblVideo.grid(column=0, row=2, columnspan=2)  # Ubicar el label ocupando dos columnas

# Iniciar el loop principal de la interfaz gráfica
root.mainloop()  # Mantener la ventana activa y escuchando eventos
