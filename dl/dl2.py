# -*- coding: utf-8 -*-
"""DL Assignment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMhN_ZhkieLnf5H7M6wdup-7PUnTICPS

Multiclass classification using Deep Neural Networks: Example: Use the OCR letter 
recognition datasethttps://archive.ics.uci.edu/ml/datasets/letter+recognition
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from yellowbrick.classifier import ConfusionMatrix
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

dataset = pd.read_csv("./letter-recognition.data", sep = ",")
dataset.head(10)

X = dataset.iloc[:, 1 : 17]
Y = dataset.select_dtypes(include = [object])
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size = 0.20, random_state = 10)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_validation = scaler.transform(X_validation)

mlp = MLPClassifier(hidden_layer_sizes = (250, 300), max_iter = 1000000, activation = 'logistic')
cm = ConfusionMatrix(mlp, classes="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(','))

cm.fit(X_train, Y_train.values.ravel())
cm.score(X_validation, Y_validation)

predictions = cm.predict(X_validation)

print("Accuracy: ", accuracy_score(Y_validation, predictions))
print("Confusion matrix:",confusion_matrix(Y_validation, predictions))
print("Classification report",classification_report(Y_validation, predictions, digits=5))