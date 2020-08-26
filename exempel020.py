import cv2
import numpy as np

# Load two images
img1 = cv2.imread('trapeador.jpg')

## Espacio de color RGB
# A partir de los tres colores "básicos" (primarios) se pueden generar
# muchos otros, por lo que estos tres colores determinan el espacio de
# colores. Se puede ver este espacio como una especie de cubo con
# coordenadas cartesianas tridimensionales
cv2.imshow('Espacio RGB',img1)
cv2.waitKey(0)

# Escala de grises
img1gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grigio',img1gray)
cv2.waitKey(0)

'''
%% Modelo de color CIE 1931 XYZ
% Es uno de los primeros espacios de color definidos matemáticamente. 
% La idea es que el concepto de color puede ser dividido en dos partes:
% brillo y cromaticidad. Por parte del brillo, se considera por ejemplo que
% el color blanco es un color brillante mientras que el gris es una forma
% menos brillante del blanco, lo que indica que lo que cambia es el brillo
% no la cromaticidad.
'''
img1XYZ = cv2.cvtColor(img1,cv2.COLOR_BGR2XYZ)
cv2.imshow('XYZ',img1XYZ)
cv2.waitKey(0)

'''
%% Modelo de color HSV
% Hue Saturation Value, Matiz, Saturación, Valor
% Se trata de una transformación no lineal del espacio de color RGB. Este
% modelo de color a diferencia del espacio RGB se puede ver como un cono,
% donde se representa:
% Matiz, es el ángulo de la cara del cono, por lo que tendrá valores de 0°
% a 360° (que también se toma de 0 a 100%), donde cada valor representa un
% color
% Saturación, representa como la distancia al eje del cono,
% Valor es la altura en el eje blanco negro
'''
img1HSV = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',img1HSV)
cv2.waitKey(0)

'''
Modelo de colo LAB
Cuenta con tres componentes:
L - Luminosidad  (Intensidad)
a - componente de color que va de verde a magenta
b - componente de color que va de azul a amarillo
Este es diferente del espacio de color RGB en que el componente de luminosidad
se encuentra separado en de las tonalidades de los tres canales de color.
Mientras que los otros dos canales codifican el color

Tiene las siguiente propiedades:
* Uniforma perceptualmente el espacio de color el cual aproxima como percibimos el color
* Indepenediente del dispositivo
* Esta relacionado con el espacio de color RGB por un a ecuación de transformación compleja
'''
img1Lab = cv2.cvtColor(img1,cv2.COLOR_BGR2Lab)
cv2.imshow('Lab - Color',img1Lab)
cv2.waitKey(0)

'''
% Este formato codifica la luminosidad, la cromancia (esto es la
% información del color de la imagen)
% Una vez que se convierte la imagen "data_YCBCR" es un arreglo
% tridimensional, del estilo M x N x 3, donde:
% M - ancho de la imagen
% N - alto de la imagen
% y las 3 capas son:
% (1) Luminancia Y (componente de luminosidad)
%   Y = 0.299 R + 0.587 G + 0.114 B
% (2) Crominancia Cb (diferencia de azul)
% (3) Crominancia Cr (diferencia de rojo)
'''
img1YCrCb = cv2.cvtColor(img1,cv2.COLOR_BGR2YCrCb)
cv2.imshow('YCrCb',img1YCrCb)
cv2.waitKey(0)

cv2.destroyAllWindows()