#! /usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

training_set = pd.read_csv('knn_sklearn_pandas_training_set.csv')
testing_set = pd.read_csv('knn_sklearn_pandas_testing_set.csv')

cols_1 = ['shoe size', 'height']
cols_2 = ['class']

training_inputs = training_set.as_matrix(cols_1)
training_outputs = training_set.as_matrix(cols_2)

testing_inputs = testing_set.as_matrix(cols_1)
testing_outputs = testing_set.as_matrix(cols_2)

knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
knn.fit(training_inputs, training_outputs.ravel())
output = knn.predict(testing_inputs)

correct_answers = 0.0
for i in range(len(output)):
    if testing_outputs[i][0] == output[i]:
        correct_answers += 1

print(correct_answers / len(output))
