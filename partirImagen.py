# Librerias a importar
# Librería OpenCV para procesamiento de imágenes
import cv2
# Librería adicional para mostrar imágenes en colab
from google.colab.patches import cv2_imshow
# Análisis numéricos
import numpy as np
# Graficación
import matplotlib.pyplot as mp

# Leer imagen de la raíz del Drive
# JPG JPEG GIF PNG BMP GIF TIFF
imagen = cv2.imread('drive//MyDrive//imagen.jpg')

# Mostrar la imagen
cv2_imshow(imagen)

# Obtener las características de tamaño y guardarlas
M, N, _ = imagen.shape
print(f"Imagen tamaño {N}x{M}")

# Se puede mostrar solamente la mitad de la imagen
# Hay que recordar que la imagen es de tamaño MxNx3
# Luego se muestra solamente la parte superior de la imagen
cv2_imshow(imagen[:int(M/2),:,:])

# Y la parte derecha de la imagen
cv2_imshow(imagen[:,:int(N/2),:])

# Cambiar la mitad de la imagen de la derecha a la izquierda y visceversa
# Primero se crea una nueva imagen, todo en cero
nueva = np.zeros(imagen.shape, imagen.dtype)
# primero se pasa la parte izquierda de la imagen a la derecha de la nueva
nueva[:,int(N/2):N,:] = imagen[:,:int(N/2),:]
nueva[:,:int(N/2),:] = imagen[:,int(N/2):N,:]
# Mostrarla
cv2_imshow(nueva)