import cv2
import numpy as np
import matplotlib.pyplot as mp

# Función para mostrar varias imágenes
def plot_imgs(images, titles):
  fig, axs = mp.subplots(nrows = 1, ncols = len(images), figsize = (15, 15))
  for i, p in enumerate(images):
    axs[i].imshow(p, 'gray')
    axs[i].set_title(titles[i])
  mp.show()

# Se la abro... (la imagen)
img = cv2.imread('gato.jpg')
# Características de la imagen
alto, ancho, _ = img.shape

# olvide pasar la imagen a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Estoy bien grifo
borroso = cv2.GaussianBlur(gris, (9, 9), 0)

# Detetor de bordes por Canny
pelos = cv2.Canny(borroso, 15, 100)
cv2.imshow("Ya vámonos a ponernos locos", pelos)

# Transformaciones morfológicas
# Dilatación
# Kernel de 1's
kernel = np.ones((3,3), np.uint8)
dilatado = cv2.dilate(pelos, kernel, iterations = 3)
cv2.imshow("No te vayas", dilatado)

# Erosión
erosion = cv2.erode(dilatado, kernel, iterations = 2)
cv2.imshow("Coffee no", erosion)

# Apertura (erosión seguida de dilatación)
# Utilizada preferentemente para eliminar ruido o
# en su caso, detalles que no representan exactamente bordes
# Este al tender a "eliminar" o colocar en 0 los píxeles
# (tal como si fuera profesor de UPIIH), es mejor usar
# tra suna dilatación o donde los bordes sean gruesos
apertura = cv2.morphologyEx(dilatado, cv2.MORPH_OPEN, kernel)
cv2.imshow("Ya se acaboooo", apertura)

# Cerradura (dilatación y luego erosión)
cerradura = cv2.morphologyEx(pelos, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Ya me dió sueño", cerradura)

# Gradiente morfológico
# En primer lugar aplica una erosión y una dilatación individual
# y después, calcula la diferencia entre las imágenes
# erosionada y dilatada
morfo = cv2.morphologyEx(pelos, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Todos reprobados", morfo)

# Top Hat
# En este caso se realiza una apertura de la imagen y
# se encuentra la diferencia entre la imagen entrada y
# la de apertura
morfoHat = cv2.morphologyEx(pelos, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Quién soy?", morfoHat)
# Es interesante ver el resultado al usar la imagen en
# escala de grises
# los valores han de subirse un 127, puesto que, lo que se
# obtiene es pequeño
morfoHat2 = cv2.morphologyEx(borroso+127, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Ya saquen!", morfoHat2)

# Black Hat
# Realiza la operación inversa a Top Hat, resaltando
# características
morfoBHat = cv2.morphologyEx(pelos, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("No toquen", morfoBHat)
# Sobre la de escala de grises
morfoBHat2 = cv2.morphologyEx(borroso+127, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Ya saquen x2!", morfoBHat2)

# Compendio de todas las imágenes
plot_imgs(
[gris, borroso, pelos, dilatado, erosion, apertura, cerradura, morfo, morfoHat, morfoBHat],
["Original","Filtro gaussiano","Canny","Dilatación","Erosión","Apertura","Cerradura","Gradiente morfológico","Top Hat","Black Hat"]
)

cv2.waitKey(0)
cv2.destroyAllWindows()
