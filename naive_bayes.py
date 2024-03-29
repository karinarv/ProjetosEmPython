# -*- coding: utf-8 -*-
"""Naive Bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15leLWbuVNiCLkMEmI-tyEn_dsP45ZRU-
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder#fazer conversão de string para numérico
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB#Não trabalha com dados categóricos

from sklearn.tree import DecisionTreeClassifier

import graphviz
from sklearn.tree import export_graphviz

from yellowbrick.classifier import ConfusionMatrix

from google.colab import drive
drive.mount('/content/gdrive')

credito = pd.read_csv('Credit.csv')

credito.info()

credito.head()

x = credito.iloc[:,0:20].values # valores em array

x

y = credito.iloc[:,20].values

# converter os previsores, criar uma transformação de string p números
label = LabelEncoder() #chama biblioteca

x[:,0] = label.fit_transform(x[:,0])
x[:,2] = label.fit_transform(x[:,2])
x[:,3] = label.fit_transform(x[:,3])
x[:,5] = label.fit_transform(x[:,5])
x[:,6] = label.fit_transform(x[:,6])
x[:,8] = label.fit_transform(x[:,8])
x[:,9] = label.fit_transform(x[:,9])
x[:,11] = label.fit_transform(x[:,11])
x[:,13] = label.fit_transform(x[:,13])
x[:,14] = label.fit_transform(x[:,14])
x[:,16] = label.fit_transform(x[:,16])
x[:,18] = label.fit_transform(x[:,18])
x[:,19] = label.fit_transform(x[:,19])

x #Strings viraram numeros

x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)

naives = GaussianNB()

naives.fit(x_treino,y_treino)

predicao = naives.predict(x_teste)

print(confusion_matrix(y_teste,predicao))

print(classification_report(y_teste,predicao))

print(accuracy_score(y_teste,predicao))

graf = ConfusionMatrix(GaussianNB())
graf.fit(x_treino,y_treino)
graf.score(x_teste,y_teste)
graf.poof()

"""## Saiu alto onde não podia, o 55 é uma pessoa que não pagou e foi habilitado que pagaram, e os que pagaram e não foi habilitado é de 29

"""

credito_n = pd.read_csv('NovoCredit.csv')

credito_n.info()

credito_n = credito_n.iloc[:,0:20].values

credito_n[:,0] = label.fit_transform(credito_n[:,0])
credito_n[:,2] = label.fit_transform(credito_n[:,2])
credito_n[:,3] = label.fit_transform(credito_n[:,3])
credito_n[:,5] = label.fit_transform(credito_n[:,5])
credito_n[:,6] = label.fit_transform(credito_n[:,6])
credito_n[:,8] = label.fit_transform(credito_n[:,8])
credito_n[:,9] = label.fit_transform(credito_n[:,9])
credito_n[:,11] = label.fit_transform(credito_n[:,11])
credito_n[:,13] = label.fit_transform(credito_n[:,13])
credito_n[:,14] = label.fit_transform(credito_n[:,14])
credito_n[:,16] = label.fit_transform(credito_n[:,16])
credito_n[:,18] = label.fit_transform(credito_n[:,18])
credito_n[:,19] = label.fit_transform(credito_n[:,19])

naives.predict(credito_n)

