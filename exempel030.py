from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow y tf.keras, el cual es una API de alto nivel para construir y entrenar modelos
import tensorflow as tf
from tensorflow import keras
# import cv2

# Librerías auxiliares
import numpy as np
import matplotlib.pyplot as plt

# Mostrar la versión del TensorFlow
print(tf.__version__)

# Descargar las imágenes para entrenar del grupo de datos Fashion-MINST
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# train_images y train_labels son el conjunto de entrenamiento, los datos del modelo utilizados para aprender
# test_images y test_labels son el conjunto de prueba

# Las imágenes son arreglos de NumPy de 28x28 con los valores de los pixeles entre 0 y 255.
# las etiquetas son un arreglo de enteros en un intervao de 0 a 9
'''
	Etiqueta		Clase
	0				T-shirt/Top
	1				Trouser
	2				Pullover
	3				Dress
	4				Coat
	5				Sandal
	6				Shirt
	7				Sneaker
	8				Bag
	9				Ankle boot
'''
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# formato de los datos
train_images.shape

# Longitud de las etiquetas de entrenamiento
len(train_labels)

# Cada etiqueta es un entero entre 0 y 9
train_labels

# Existen 10000 imágenes en el conjunto de prueba
test_images.shape

# Longitud de las etiquetas de prueba
len(test_labels)

# Mostrar una de las figuras de entrenamiento
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
# cv2.imshow('Trenamiento', train_images[0])

# Normalizar los datos
train_images = train_images / 255.0
test_images = test_images / 255.0

# Mostrar las figuras con sus etiquetas
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# Aquí entonces se acomodan los datos para que ingresen a la red neuronal
# Primero las matrices de imagen 28x28 se colocan en un vector de 28x28 = 784
# Después se indica que la red tendrá 128 nodos con una función de activación
# Finalmente se coloca una capa de 10 nodos que regresará un arreglo de 10 probabilidades
# que corresponden a las etiquetas de las imágenes
# Funciones de activación:
# relu -> Rectified Linear Unit
# softmax -> Función exponencial normalizada
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Posteriormente se tiene que configurar el modelo :
# Optimizador: Esto es como el modelo se actualiza con base en en lo que ve de la función loss
# Función loss: Mide cuan preciso es el modelo durante el entrenamiento. Se desea minimizar la función para guiar al modelo en la dirección correcta
# Métricas: Utilzadas para monitorear los pasos del entrenamiento y pruebas
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo con los datos de las imágenes y etiquetas de entrenamiento
# considerar cuántas épocas se requieren para entrenar el modelo
model.fit(train_images, train_labels, epochs=10)

# Posteriormente se tiene que validar que tan bueno resulto el modelo
# probando con los conjuntos de prueba
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

# Para hacer predicciones se puede tomar el entonces el conjunto de imágenes de prueba
predictions = model.predict(test_images)

# Se puede observar la primera predicción
predictions[0]

# Se observa cual es el que tiene el valor máximo, que representaría el que tiene la mayor
# probabilidad de que sea la etiqueta
np.argmax(predictions[0])

# Se compara con la etiqueta de prueba
test_labels[0]

# Se generan funciones para graficar como se parecen en un conjunto total de previsión
# las 10 clases
def plot_image(i, predictions_array, true_label, img):
 predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
 plt.grid(False)
 plt.xticks([])
 plt.yticks([])

 plt.imshow(img, cmap=plt.cm.binary)

 predicted_label = np.argmax(predictions_array)
 if predicted_label == true_label:
  color = 'blue'
 else:
  color = 'red'

 plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label], 100*np.max(predictions_array), class_names[true_label]), color=color)

def plot_value_array(i, predictions_array, true_label):
 predictions_array, true_label = predictions_array[i], true_label[i]
 plt.grid(False)
 plt.xticks([])
 plt.yticks([])
 thisplot = plt.bar(range(10), predictions_array, color="#777777")
 plt.ylim([0, 1])
 predicted_label = np.argmax(predictions_array)

 thisplot[predicted_label].set_color('red')
 thisplot[true_label].set_color('blue')

# Se observa la previsión de la imagen en la posición 0
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()


# Tomar una imagen del grupo de datos
img = test_images[0]
print(img.shape)

# Añade una imagen en un lote que solo tiene un miembro
img = (np.expand_dims(img,0))
print(img.shape)

# Se coloca la etiqueta correcta para la imagen
predictions_single = model.predict(img)
print(predictions_single)

# Graficar que tanto se parece
plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()

np.argmax(predictions_single[0])