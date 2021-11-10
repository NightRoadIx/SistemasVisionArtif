# -*- coding: utf-8 -*-
"""
Created on Tue Nov 666 666:666:666 666

@author: s_bio
"""

from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk

import cv2
import imutils
import numpy as np

# Función para la selección de la imagen
def elegir_imagen():
    # Especificar los tipos de archivos que pueden ser seleccionados
    path_image = filedialog.askopenfilename(filetypes = [
        ("imagen", ".jpeg"),
        ("imagen", ".png"),
        ("imagen", ".jpg")])

    if len(path_image) > 0:
        global image

        # Lectura de la imagen de entrada y redimensionarla
        image = cv2.imread(path_image)
        image= imutils.resize(image, height=380)

        # Visualizar la imagen en la GUI
        imageToShow= imutils.resize(image, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow )
        img = ImageTk.PhotoImage(image=im)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

        # Colocar una etiqueta con la IMAGEN DE ENTRADA
        lblInfo1 = Label(root, text="IMAGEN DE ENTRADA:")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)

        # Al momento de leer la imagen de entrada, se coloca la
        # imagen de salida y se limpia la selección del radiobutton
        lblOutputImage.image = ""
        selected.set(0)

# Función para la detección del color
def deteccion_color():
    global image
    if selected.get() == 1:
        # Rojo
        rangoBajo1 = np.array([0, 140, 90], np.uint8)
        rangoAlto1 = np.array([8, 255, 255], np.uint8)
        rangoBajo2 = np.array([160, 140, 90], np.uint8)
        rangoAlto2 = np.array([180, 255, 255], np.uint8)

    if selected.get() == 2:
        # Amarillo
        rangoBajo = np.array([10, 98, 0], np.uint8)
        rangoAlto = np.array([25, 255, 255], np.uint8)

    if selected.get() == 3:
        # Azul celeste
        rangoBajo = np.array([88, 104, 121], np.uint8)
        rangoAlto = np.array([99, 255, 243], np.uint8)
        
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if selected.get() == 1:
        # Se realiza la detección del color rojo
        maskRojo1 = cv2.inRange(imageHSV, rangoBajo1, rangoAlto1)
        maskRojo2 = cv2.inRange(imageHSV, rangoBajo2, rangoAlto2)
        mask = cv2.add(maskRojo1, maskRojo2)
    else:
        # Esto genera la detección del azul celeste y el amarillo
        mask = cv2.inRange(imageHSV, rangoBajo, rangoAlto)

    mask = cv2.medianBlur(mask, 7)
    colorDetected = cv2.bitwise_and(image, image, mask=mask)

    # Fondo en color gris
    invMask = cv2.bitwise_not(mask)
    bgGray = cv2.bitwise_and(imageGray, imageGray, mask=invMask)

    # Sumamos bgGray y colorDetected
    finalImage = cv2.add(bgGray, colorDetected)
    imageToShowOutput = cv2.cvtColor(finalImage, cv2.COLOR_BGR2RGB)

    # Para visualizar la imagen en lblOutputImage en la GUI
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    # Label IMAGEN DE SALIDA
    lblInfo3 = Label(root, text="IMAGEN DE SALIDA:", font="bold")
    lblInfo3.grid(column=1, row=0, padx=5, pady=5)
    
# MAIN
# Generar la ventana principal
root = Tk()

# Etiqueta donde se presentará la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

# Etiqueta donde se presentará la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column=1, row=1, rowspan=6)

# Se generan los radiobuttons y su posición en la ventana
selected = IntVar()
rad1 = Radiobutton(root, text='Rojo', width=25,value=1, variable=selected, command= deteccion_color)
rad2 = Radiobutton(root, text='Amarillo',width=25, value=2, variable=selected, command= deteccion_color)
rad3 = Radiobutton(root, text='Azul celeste',width=25, value=3, variable=selected, command= deteccion_color)
rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=6)

# Crear el botón patra elegir la imagen de entrada
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5, pady=5)

# Aquí es donde va el loop
root.mainloop()