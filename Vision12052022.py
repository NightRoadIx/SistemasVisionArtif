# Usar el set de datos de Google Drive compartido
# https://drive.google.com/drive/folders/1ZE7oSmniLADTv_3aVcgajXWZxVUp8r_C?usp=sharing

# Cargar la información desde el Drive
from google.colab import drive 
drive.mount('/content/gdrive')

# Directorio
dir_path = "gdrive/My Drive/Dataset/Frutas/"

# Librerías a importar
import numpy as np
import pandas as pd
import cv2
import os 
from PIL import Image

# Revisar el directorio
import os
for dirname, _, filenames in os.walk(dir_path):
    for filename in filenames:
        print(os.path.join(dirname, filename))

images  =  []       
labels  =  [] 
train_path  =  'gdrive/My Drive/Dataset/Frutas/train_zip/train'
for filename in os.listdir('gdrive/My Drive/Dataset/Frutas/train_zip/train'):
    if filename.split('.')[1]  ==  'jpg':
        img  =  cv2.imread(os.path.join(train_path,filename))
        arr = Image.fromarray(img,'RGB')
        img_arr = arr.resize((50,50))
        labels.append(filename.split('_')[0])
        images.append(np.array(img_arr))

# Ver las etiquetas
np.unique(labels)

# Codificar las etiquetas de forma numérica
from sklearn.preprocessing import LabelEncoder
lb_encod  =  LabelEncoder()
labels = pd.DataFrame(labels)
labels = lb_encod.fit_transform(labels[0])
labels

# Observar una imagen
# TODO: Modificar de RGB a BRG
import matplotlib.pyplot as plt
figure = plt.figure(figsize = (8,8))
ax = figure.add_subplot(121)
ax.imshow(images[1])
bx = figure.add_subplot(122)
bx.imshow(images[60])
plt.show()

# Se preprocesarán los datos
# Salvar el arreglo de imágenes y sus etiquetas
images = np.array(images)
np.save("imagenes",images)
np.save("etiquetas",labels)

# Cargar las imágenes y etiquetas
image = np.load("imagenes.npy",allow_pickle = True)
labels = np.load("etiquetas.npy",allow_pickle = True)

img_shape  = np.arange(image.shape[0])
np.random.shuffle(img_shape)
image = image[img_shape]
labels = labels[img_shape]

num_classes = len(np.unique(labels))
len_data = len(image)
x_train, x_test = image[(int)(0.1*len_data):],image[:(int)(0.1*len_data)]
y_train,y_test = labels[(int)(0.1*len_data):],labels[:(int)(0.1*len_data)]

import tensorflow as tf
y_train = tf.keras.utils.to_categorical(y_train,num_classes)
y_test = tf.keras.utils.to_categorical(y_test,num_classes)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Conv2D,MaxPooling2D,Dropout,Flatten,MaxPool2D
from tensorflow.keras.optimizers import RMSprop,Adam
from tensorflow.keras.layers import Activation, Convolution2D, Dropout, Conv2D,AveragePooling2D, BatchNormalization,Flatten,GlobalAveragePooling2D
from tensorflow.keras import layers
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import ModelCheckpoint,ReduceLROnPlateau

l2_reg = 0.001
opt = Adam(lr = 0.001)

# Definir el modelo de la Red
cnn_model  =  Sequential()
cnn_model.add(Conv2D(filters = 32, kernel_size = (2,2), input_shape = (50,50, 3), activation = 'relu',kernel_regularizer = l2(l2_reg)))
cnn_model.add(MaxPool2D(pool_size = (2,2)))
cnn_model.add(Conv2D(filters = 64, kernel_size = (2,2), activation = 'relu',kernel_regularizer = l2(l2_reg)))
cnn_model.add(MaxPool2D(pool_size = (2,2)))
cnn_model.add(Conv2D(filters = 128, kernel_size = (2,2), activation = 'relu',kernel_regularizer = l2(l2_reg)))
cnn_model.add(MaxPool2D(pool_size = (2,2)))
cnn_model.add(Dropout(0.1))

cnn_model.add(Flatten())

cnn_model.add(Dense(64, activation = 'relu'))
cnn_model.add(Dense(16, activation = 'relu'))
cnn_model.add(Dense(4, activation = 'softmax'))

# Modelo
cnn_model.summary()

# Compilar el modelo
cnn_model.compile(loss = 'categorical_crossentropy', optimizer = opt, metrics = ['accuracy'])

# Entrenar el modelo
# Guardar los pesos del entrenamiento en un archivo de manera temporal
file1 = 'weights.hdf5'
checkpoint = ModelCheckpoint(file1, monitor='loss', verbose=1, save_best_only=True, mode='min')
history = cnn_model.fit(x_train,y_train,batch_size = 128,epochs = 110,verbose = 1,validation_split = 0.33)

# Revisar el rendimiento
scores  =  cnn_model.evaluate(x_test, y_test, verbose = 1)
print('Prueba pérdida:', scores[0])
print('Prueba exactitud:', scores[1])

# Visualizar el rendimiento
figure = plt.figure(figsize = (10,5))
ax = figure.add_subplot(121)
ax.plot(history.history['accuracy'])
ax.plot(history.history['val_accuracy'])
ax.legend(['Training Accuracy','Val Accuracy'])
bx = figure.add_subplot(122)
bx.plot(history.history['loss'])
bx.plot(history.history['val_loss'])
bx.legend(['Training Loss','Val Loss'])

# Pruebas
test_path  =  'gdrive/My Drive/Dataset/Frutas/test_zip/test'
t_labels = []
t_images = []
for filename in os.listdir('gdrive/My Drive/Dataset/Frutas/test_zip/test'):
    if filename.split('.')[1]  ==  'jpg':
        img  =  cv2.imread(os.path.join(test_path,filename))
        arr = Image.fromarray(img,'RGB')
        img_arr = arr.resize((50,50))
        t_labels.append(filename.split('_')[0])
        t_images.append(np.array(img_arr))

test_images = np.array(t_images)
np.save("test_images.npy",test_images)
test_image = np.load("test_images.npy",allow_pickle = True)

pred = np.argmax(cnn_model.predict(test_image),axis = 1)

test_image = np.expand_dims(test_image[25],axis = 0)
pred_test = np.argmax(cnn_model.predict(test_image),axis = 1)

print(cnn_model.predict(test_image))
print(pred)
print(pred_test)