from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

def iniciar():
    """
        Función para iniciar la captura de video
    :return: None
    """
    # Variable global cap
    global cap
    # Capturar el video del dispositivo configurado como 0
    # armar el objeto
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Llamar a la función visualizar
    visualizar()

def visualizar():
    """
        Función para visualizar la imagen en una etiqueta
        de la interfaz gráfica de usuario
    :return: None
    """
    # Mantener la variable global cap
    global cap
    # Si cap existe
    if cap is not None:
        # Lectura de lo que tiene el objeto
        # Regresa si fue exitoso y la matriz leída
        ret, frame = cap.read()
        # Si se leyó algo en particular
        if ret == True:
            # Redimensionar la imagen con ancho 640 px
            frame = imutils.resize(frame, width=640)
            # Cambiar de BGR a RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Modificar a tipo Image de Pillow desde un arreglo
            im = Image.fromarray(frame)
            # Tipo de imagen PhotoImage
            img = ImageTk.PhotoImage(image=im)

            # Configurar la etiqueta para mostrar la imagen
            lblVideo.configure(image=img)
            # Modificar el atributo image como la imagen tipo PhotoImage
            lblVideo.image = img
            #
            lblVideo.after(10, visualizar)
        else:   # En caso contrario, el dispositivo no leyó nada
            lblVideo.image = ""
            # Liberar el objeto
            cap.release()

def finalizar():
    """
        Función para finalizar la imagen
    :return: None
    """
    # Se mantiene la variable global
    global cap
    # Se libera el objeto
    cap.release()

cap = None
root = Tk()

# Botón para iniciar la muestra del "video" o secuencia de imágenes
btnIniciar = Button(root, text="Iniciar", width=45, command=iniciar)
# Colocar el botón en la rejilla
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

# Botón para finalizar el "video"
btnFinalizar = Button(root, text="Finalizar", width=45, command=finalizar)
# Colocar el botón en la rejilla
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

# Etiqueta donde se mostrará el video
lblVideo = Label(root)
# Colocar la etiqueta en la rejilla
lblVideo.grid(column=0, row=1, columnspan=2)

# Ciclar el programa para que se muestre la interfaz
# una especie de loop() como en Arduino
root.mainloop()
