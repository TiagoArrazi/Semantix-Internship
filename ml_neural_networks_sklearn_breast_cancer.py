#! /usr/bin/env python3

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

cancer = load_breast_cancer()
X, y = cancer.data, cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30), max_iter=1000)
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)

for prediction, y  in zip(predictions, y_test):
        print('prediction: {}, expected: {}'.format(prediction, y))

print('Score: {}\n'.format(mlp.score(X_test, y_test)))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
