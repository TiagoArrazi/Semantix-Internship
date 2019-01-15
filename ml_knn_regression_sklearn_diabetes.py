#! /usr/bin/env python3

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error


diabetes = datasets.load_diabetes()
x, y = diabetes.data, diabetes.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
knn = KNeighborsRegressor(n_neighbors=91, p=2)
knn.fit(x_train, y_train)
outputs = knn.predict(x_test)

print(mean_squared_error(y_test, outputs))
