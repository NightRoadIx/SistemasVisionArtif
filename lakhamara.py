# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:31:59 2022

@author: s_bio
"""

from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils


def iniciar():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualiza()
    
def visualiza():
    global cap
    # Que "haiga" algo en la cámara
    if cap is not None:
        ret, frame = cap.read()
        # Cuando ya se tiene una imagen
        if ret == True:
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            
            lblVideo.configure(image=img)
            lblVideo.image = img
            # mandar a llamar la función visualiza
            # cada 10 ms
            lblVideo.after(10, visualiza)
        else:
            lblVideo.image = ""
            cap.release()

def finalizar():
    global cap
    cap.release()


cap = None
root = Tk()

btnIniciar = Button(root, text="Iniciar", width=45, command=iniciar)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(root, text="Finalizar", width=45, command=finalizar)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)

root.mainloop()