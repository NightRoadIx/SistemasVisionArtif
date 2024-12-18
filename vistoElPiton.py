# Importar librerías necesarias
from tkinter import *  # Para la interfaz gráfica
from PIL import Image, ImageTk  # Para manejo de imágenes en la GUI
import cv2  # Para procesamiento de video e imágenes
import imutils  # Para redimensionar imágenes
import mediapipe as mpipe  # Framework Mediapipe para detección

# Función para iniciar la cámara
def iniciar():
    """
    Inicia la cámara y configura la función visualizar para procesar y mostrar el video.
    """
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Capturar video del dispositivo de cámara
    visualizar()

# Función para procesar y visualizar el video en tiempo real
def visualizar():
    """
    Lee y procesa los fotogramas de la cámara para mostrar en la interfaz gráfica.
    Si está activado FaceMesh o HandLandmarks, se aplican las detecciones correspondientes.
    """
    global cap, facemesh_active, hand_active, facemesh, hands
    if cap is not None:
        ret, frame = cap.read()  # Leer un fotograma de la cámara
        if ret:
            frame = imutils.resize(frame, width=640)  # Redimensionar el fotograma
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir a RGB

            # Si está activado FaceMesh
            if facemesh_active:
                results = facemesh.process(frame_rgb)  # Procesar detección FaceMesh
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        mpipe.solutions.drawing_utils.draw_landmarks(
                            frame, face_landmarks,
                            mpipe.solutions.face_mesh.FACEMESH_TESSELATION,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=mpipe.solutions.drawing_styles.get_default_face_mesh_tesselation_style()
                        )

            # Si está activado HandLandmarks
            if hand_active:
                results = hands.process(frame_rgb)  # Procesar detección HandLandmarks
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mpipe.solutions.drawing_utils.draw_landmarks(
                            frame, hand_landmarks,
                            mpipe.solutions.hands.HAND_CONNECTIONS,
                            landmark_drawing_spec=mpipe.solutions.drawing_styles.get_default_hand_landmarks_style(),
                            connection_drawing_spec=mpipe.solutions.drawing_styles.get_default_hand_connections_style()
                        )

            # Convertir de nuevo para mostrar en la GUI
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            # Actualizar la imagen en el label
            lblVideo.configure(image=img)
            lblVideo.image = img

            # Llamar recursivamente a la función visualizar
            lblVideo.after(10, visualizar)
        else:
            lblVideo.image = ""
            cap.release()  # Liberar la cámara si no hay más fotogramas

# Función para activar/desactivar FaceMesh
def activar_facemesh():
    """
    Activa o desactiva la detección FaceMesh. Desactiva HandLandmarks si está activo.
    """
    global facemesh_active, hand_active
    if facemesh_active:
        facemesh_active = False
        btnFaceMesh.config(relief=RAISED)
        btnHandLandmarks.config(state=NORMAL)  # Habilitar el botón de HandLandmarks
    else:
        facemesh_active = True
        hand_active = False
        btnFaceMesh.config(relief=SUNKEN)
        btnHandLandmarks.config(state=DISABLED)  # Deshabilitar el botón de HandLandmarks

# Función para activar/desactivar HandLandmarks
def activar_handlandmarks():
    """
    Activa o desactiva la detección HandLandmarks. Desactiva FaceMesh si está activo.
    """
    global hand_active, facemesh_active
    if hand_active:
        hand_active = False
        btnHandLandmarks.config(relief=RAISED)
        btnFaceMesh.config(state=NORMAL)  # Habilitar el botón de FaceMesh
    else:
        hand_active = True
        facemesh_active = False
        btnHandLandmarks.config(relief=SUNKEN)
        btnFaceMesh.config(state=DISABLED)  # Deshabilitar el botón de FaceMesh

# Función para finalizar la cámara
def finalizar():
    """
    Libera la cámara y detiene la captura de video.
    """
    global cap
    cap.release()
    lblVideo.image = ""  # Limpiar la imagen en el label

# Configurar Mediapipe para FaceMesh y HandLandmarks
facemesh = mpipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
hands = mpipe.solutions.hands.Hands()

# Variables globales para manejar el estado de las detecciones
cap = None
facemesh_active = False
hand_active = False

# Crear la ventana principal
root = Tk()

# Botón para iniciar la cámara
btnIniciar = Button(root, text="Iniciar", width=45, command=iniciar)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

# Botón para finalizar la cámara
btnFinalizar = Button(root, text="Finalizar", width=45, command=finalizar)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

# Botón para activar/desactivar FaceMesh
btnFaceMesh = Button(root, text="Activar FaceMesh", width=45, command=activar_facemesh)
btnFaceMesh.grid(column=0, row=1, padx=5, pady=5)

# Botón para activar/desactivar HandLandmarks
btnHandLandmarks = Button(root, text="Activar HandLandmarks", width=45, command=activar_handlandmarks)
btnHandLandmarks.grid(column=1, row=1, padx=5, pady=5)

# Label para mostrar el video
lblVideo = Label(root)
lblVideo.grid(column=0, row=2, columnspan=2)

# Ejecutar la interfaz gráfica
root.mainloop()
