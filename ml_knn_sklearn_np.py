#! /usr/bin/env python3

'''
Dataset: https://archive.ics.uci.edu/ml/datasets/Balance+Scale

Attribute Info:

1. Class Name: 3 (L=1, B=2, R=3)
2. Left-Weight: 5 (1, 2, 3, 4, 5) 
3. Left-Distance: 5 (1, 2, 3, 4, 5)
4. Right-Weight: 5 (1, 2, 3, 4, 5)
5. Left-Weight: 5 (1, 2, 3, 4, 5)


625 samples, 4 attributes, 3 possible classes

'''

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from numpy import array, genfromtxt

inputs = genfromtxt('balance_scale_dataset.txt', delimiter=',', usecols=(1,2,3,4))
outputs = genfromtxt('balance_scale_dataset.txt', delimiter=',', usecols=(0))
training_inputs, testing_inputs, training_outputs, testing_outputs = train_test_split(
                                                                     inputs, 
                                                                     outputs, 
                                                                     test_size=0.3, 
                                                                     random_state=42)

knn = KNeighborsClassifier(n_neighbors=17, p=2) # p=2 means Euclidean Distance(default)
knn.fit(training_inputs, training_outputs)
labels = knn.predict(testing_inputs)
print(f'Accuracy: {(knn.score(testing_inputs, testing_outputs) * 100):.2f}%')
print(f'Training Inputs: {len(training_inputs)} {((len(training_inputs) / ((len(training_inputs) + len(testing_inputs)))) * 100):.2f}% of the dataset')
print(f'Testing Inputs: {len(testing_inputs)} {((len(testing_inputs) / ((len(training_inputs) + len(testing_inputs)))) * 100):.2f}% of the dataset')
