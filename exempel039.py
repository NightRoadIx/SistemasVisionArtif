# Cargar las librerías
import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CARGAR IMÁGENES
# Descargar las imágenes de prueba, se componen de 60000 imágenes de 10 clases diferentes
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CONFIGURAR IMÁGENES
# Normalizar los valores de píxeles de [0, 255] a [0, 1]
# Esto es muy importante
train_images, test_images = train_images / 255.0, test_images / 255.0

# observar las características de las imágenes
print(len(train_images))
print(len(test_images))

# También se debe recordar que estas imágenes están asociadas a unas etiquetas
# las cuáles están en formato numérico
print(train_labels)

print(train_images.shape)

# Se el asigna un nombre a cada una de las etiquetas
class_names = ['avión', 'automóvil', 'ave', 'gato', 'ciervo',
               'perro', 'rana', 'caballo', 'barco', 'camión']

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    # Aquí se muestran los nombres que se le dieron a las etiquetas
    # al asociar el vector de nombres que se creo con las etiquetas 
    # del paquete de imágenes
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ARQUIETECTURA DE LA RED NEURONAL
# Generar la arquitectura de la red neuronal
model = models.Sequential()
# Esta es la primera capa de entrada, debe ser igual a como son las imágenes (32x32x3)
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten()) # Aquí los datos de "aplanan" para convertir los arreglos tridimensionales en un vector plano
model.add(layers.Dense(64, activation='relu'))
# La capa de salida corresponde a las 10 clases con las que se cuenta
model.add(layers.Dense(10))

model.summary()

# Compilar el modelo con:
# Optimizador: adam
# Pérdida: Entropía Cruzada
# Métrica: accuracy
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ENTRENAR LA RED
# Ejecutar el aprendizaje
# Se realizarán solamente 10 épocas
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# EVALUAR EL MODELO
# Evaluar la precisión del modelo
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(test_acc)

# Evaluar el modelo
plt.plot(history.history['accuracy'], label='precisión')
plt.plot(history.history['val_accuracy'], label = 'precisión_val')
plt.xlabel('Época')
plt.ylabel('Precisión')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# HACER PREDICCIONES
# La función predict de un modelo, permite realizar predicciones de a que
# clase pertencerá una entrada
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)
print(len(predictions))

# Ver una de las predicciones
predictions[1]
# Mostrar el número de la etiqueta
print(np.argmax(predictions[1]))
# Mostrar el nombre de la clase
print(class_names[train_labels[np.argmax(predictions[1])][0]])
# Mostrar la imagen de la predicción
plt.figure(figsize=(2,2))
plt.imshow(test_images[1], cmap=plt.cm.binary)
plt.show()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# SALVAR EL MODELO
# Es posible guardar un modelo ya entrenado usando la función save(), en un solo
# archivo, el cual incluye:
#  Modelos de la arquitectura
#  Valores de los pesos del modelo, aprendidos durante el entrenamiento
#  Configuración del entrenamiento del modelo
#  Optimizador y su estado, lo cual permite seguir entrenando el modelo
# Se debe guardar con la extensión .h5
model.save('modeloguarda.h5')


# Para cargar el modelo, solamente es necesario usar la función load_model de keras:
#     modelosalvado = keras.models.load_model('modeloguarda.h5')
# Lo que permite recuperar el modelo para hacer predicciones (o seguir entrenando)