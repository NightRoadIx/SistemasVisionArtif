import cv2
import numpy as np
from scipy.stats import moment
import matplotlib.pyplot as plt

# Vamos a "ler" una imagen digital
imagen = cv2.imread(r"imagen.jpg")
cv2.imshow("Original", imagen)

# Convirtiendo la imagen a escala de grises
grisImagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Escala de grises", imagen)

# Calculando el histograma de la imagen en escala de grises
histograma = cv2.calcHist([grisImagen], [0], None, [256], [0, 256])

# Normalizando el histograma
histograma = histograma.ravel()/histograma.sum()

# Calculando los primeros 4 momentos estadísticos del histograma
media = np.mean(histograma)
varianza = np.var(histograma)
asimetria = moment(histograma, moment=3)
curtosis = moment(histograma, moment=4)

# Imprimiendo los momentos estadísticos
print(f'Media: {media}')
print(f'Varianza: {varianza}')
print(f'Asimetría: {asimetria}')
print(f'Curtosis: {curtosis}')

# Graficando el histograma
plt.plot(histograma)
plt.title('Histograma')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')
plt.show()

cv2.destroyAllWindows()
