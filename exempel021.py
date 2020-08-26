import cv2
import numpy as np

image = cv2.imread('nadal.jpg')

while(1):

  # Convertir la imagen RGB a HSV
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  # Definir un intervalo del color azul en HSV
  lower_verde = np.array([25,50,50])
  upper_verde = np.array([67,255,255])
  lower_rosa1 = np.array([125,50,50])
  upper_rosa1 = np.array([167,255,255])

  # Umbralizar la imagen HSV para obtener solo los colores azules
  mask = cv2.inRange(hsv, lower_verde, upper_verde)
  mask1 = cv2.inRange(hsv, lower_rosa1, upper_rosa1)

  # Bitwise-AND mask and original image
  bola = cv2.bitwise_and(image,image, mask= mask)
  camiseta = cv2.bitwise_and(image,image, mask= mask1)
  cv2.imshow('frame',image)
  cv2.imshow('HSV',hsv)
  cv2.imshow('mask',mask)
  cv2.imshow('mask1',mask1)
  cv2.imshow('Bola',bola)
  cv2.imshow('Camiseta',camiseta)

  k = cv2.waitKey(5)
  # si pulsa q se rompe el ciclo
  if k == ord("q"):
    break

cv2.destroyAllWindows()