import numpy as np
import matplotlib.pyplot as mp

def gkern(kernlen=21, std=3):
    """
        Calcula un "kernel" del tipo Gaussiano
        de tamaño kernlen y desviación estándar std
    :param kernlen: Tamaño del kernel (valor impar) 
    :param std: Desviación estándar
    :return: kernel guassiano con media en el centro y desviación estándar std
    """
    ax = np.linspace(-(kernlen - 1) / 2., (kernlen - 1) / 2., kernlen)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(std))
    # Con esto se calcula el producto exterior de dos vectores
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

tam = 21
kernel = gkern(tam)

mp.imshow(kernel, interpolation='none')
mp.show()

# Mostrar en 3D
from matplotlib import cm
x = np.linspace(0, tam, num=tam)
y = np.linspace(0, tam, num=tam)
x, y = np.meshgrid(x, y)
fig = mp.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, kernel, cmap=cm.jet)
mp.show()
