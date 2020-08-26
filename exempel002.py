import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('endgame.jpeg',0)
# Esto es cuando se usa la librería matplotlib para abrir una imagen
# interpolation:
# 
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # Esconder los ejes X, Y
plt.show()


# Interpolación
'''methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']
'''
