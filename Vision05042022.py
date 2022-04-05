# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:01:11 2022

@author: s_bio
"""

'''
Se requiere: PIL, imutils
Que se instalan con:
    pip install pillow
    pip install imutils
'''
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np

# Seleccionar imágenes
def elegir_imagen():
    # Especificar los tipos de archivos, 
    # para elegir sólo a las imágenes
    path_image = filedialog.askopenfilename(
        filetypes = [
        ("Imagen", ".jpeg"),
        ("Imagen", ".png"),
        ("Imagen", ".jpg")
        ])

    if len(path_image) > 0:
        global image

        # Leer la imagen de entrada y la redimensionamos
        image = cv2.imread(path_image)
        image= imutils.resize(image, height=380)

        # Para visualizar la imagen de entrada en la GUI
        imageToShow= imutils.resize(image, width=180)
        # Cambiar de espacio de color BGR a RGB
        # opencv => BGR
        # PIL => RGB
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        # Cambiamos a un arreglo
        im = Image.fromarray(imageToShow)
        # Y esto a una imagen a utilizar en Tkinter
        img = ImageTk.PhotoImage(image=im)
        
        # Ubicar la imagen en la GUI
        # labelInputImage = Imagen de entrada en etiqueta
        lblInputImage.configure(image=img)
        # La imagen del widget va a ser img (RGB, vector 380x180x3)
        lblInputImage.image = img

        # Label IMAGEN DE ENTRADA
        # tkinter => "main" se llama "root", texto
        lblInfo1 = Label(root, text="IMAGEN DE ENTRADA:")
        # tkinter trabaja en una ventana con una rejilla        
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)

        # Al momento que leemos la imagen de entrada, vaciamos
        # la imagen de salida y se limpia la selección de los
        # radiobutton
        lblOutputImage.image = ""
        # selected.set(0)


# Crear la ventana principal mediante Tkinter
# Creamos el objeto "root" con el constructor Tk()
root = Tk()

# Label donde se presenta la imagen de entrada
# Creamos el objeto "lblInputImage" con el
# constructor Label(root) en la ventana principal
lblInputImage = Label(root)
lblInputImage.grid(column = 0, row = 2)

lblOutputImage = Label(root)
lblOutputImage.grid(column = 1, row = 1, rowspan = 6)

# Elegir la imagen de entrada mediante un botón
btn = Button(root, text="Elegir imagen",
             width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5, pady=5)


# Función loop estilo Arduino
# con esto ejecutamos la ventana =D
root.mainloop()