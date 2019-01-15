#! /usr/bin/env python3

import numpy as np
from sklearn import neighbors, datasets

iris = datasets.load_iris()
inputs = iris.data
outputs = iris.target

knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(inputs, outputs)
accuracy = knn.score(inputs, outputs)
print(accuracy)
