# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:25:25 2022

@author: s_bio
"""

'''
El programa require instalar mediapipe

pip install mediapipe
'''

import cv2
import mediapipe as mp
import ctypes

# Obtener el tamaño de la pantalla
user32 = ctypes.windll.user32
tamanho = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Esto ayudará a dibujar los resultados de las detecciones
mp_drawing = mp.solutions.drawing_utils
# La parte para la localización de las manos
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# with funciona como un generador de contextos, el cual permite ejecutar
# una serie de instrucciones y al finalizar las "termina" o "apaga"
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        if ret == False:
            break

        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                print(
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, ",",
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y, ",",
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z)
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,255), thickness=3, circle_radius=5),
                    mp_drawing.DrawingSpec(color=(255,0,255), thickness=4, circle_radius=5))
        
        # Colocar la ventana centrada
        cv2.namedWindow('Frame')
        cv2.moveWindow('Frame', int((tamanho[0] / 2) - width / 2), int( (tamanho[1] / 2) - height / 2 ))
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()