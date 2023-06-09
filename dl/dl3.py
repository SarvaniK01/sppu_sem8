# -*- coding: utf-8 -*-
"""DL Practical - 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z81F4d_Q7CX2EbxvSgHoFrZ75oKmx2qv

Use MNIST Fashion Dataset and create a classifier to classify fashion clothing into
categories.
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Flatten, Dense, Softmax
from keras.losses import SparseCategoricalCrossentropy

fashion = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion.load_data()

classes = ["Tshirt/top", "Trousers", "Pullover", "Dress", "Coat", "Sneakers", "Shirts", "Sandals", "Bag", "Ankleboots"]

plt.figure(figsize=(10, 10))
for i in range(25):
  plt.subplot(5,5,i+1)
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(train_images[i], cmap = plt.cm.binary)
  plt.xlabel(classes[train_labels[i]])
plt.show()

model = Sequential([Flatten(input_shape=(28, 28)), Dense(128, activation="relu"), Dense(10)])
model.compile(optimizer="adam", loss=SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Accuracy:", test_acc)

probability_model = Sequential([model, Softmax()])
predictions = probability_model.predict(test_images)

def plot_image(i, prediction_array, true_label, img):
  true_label, img = true_label[i], img[i]

  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(img, cmap = plt.cm.binary)

  predicted_label = np.argmax(prediction_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color='red'
  
  plt.xlabel('{} ({})'.format(classes[predicted_label], classes[true_label]), color=color)

plt.figure(figsize=(10,10))

for i in range(25):
  plt.subplot(5,5,i+1)
  plot_image(i, predictions[i], test_labels, test_images)
plt.show()