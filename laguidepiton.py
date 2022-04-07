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
    print(path_image)

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
        # Detectamos el color rojo
        maskRojo1 = cv2.inRange(imageHSV, rangoBajo1, rangoAlto1)
        maskRojo2 = cv2.inRange(imageHSV, rangoBajo2, rangoAlto2)
        mask = cv2.add(maskRojo1, maskRojo2)
    else:
        # Detección para el color Amarillo y Azul celeste
        mask = cv2.inRange(imageHSV, rangoBajo, rangoAlto)

    mask = cv2.medianBlur(mask, 7)
    colorDetected = cv2.bitwise_and(image, image, mask=mask)

    # Fondo en grises
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

# Creamos los radio buttons y la ubicación que estos ocuparán
selected = IntVar()
rad1 = Radiobutton(root, text='Rojo', width=25,value=1, variable=selected, command= deteccion_color)
rad2 = Radiobutton(root, text='Amarillo',width=25, value=2, variable=selected, command= deteccion_color)
rad3 = Radiobutton(root, text='Azul celeste',width=25, value=3, variable=selected, command= deteccion_color)
rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=6)

# Función loop estilo Arduino
# con esto ejecutamos la ventana =D
root.mainloop()