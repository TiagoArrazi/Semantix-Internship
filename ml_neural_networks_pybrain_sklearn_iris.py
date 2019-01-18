#! /usr/bin/env python3

import matplotlib.pyplot as plt

from sklearn import datasets
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

iris = datasets.load_iris()
X, y =  iris.data, iris.target
dataset = ClassificationDataSet(4, 1, nb_classes=3)

for sample_input, sample_output in zip(X, y):
    dataset.addSample(sample_input, sample_output)

# Partitioning data for training
training_data, partitioned_data = dataset.splitWithProportion(0.6)

# Spliting data for testing and validation
testing_data, validation_data, = partitioned_data.splitWithProportion(0.5)

network = buildNetwork(dataset.indim, 2, 2, dataset.outdim)
trainer = BackpropTrainer(network, dataset=training_data, learningrate=0.01, momentum=0.1,                          verbose=True)

training_errors, validation_errors = trainer.trainUntilConvergence(dataset=training_data,
                                                                   maxEpochs=200)
plt.plot(training_errors, 'b', validation_errors, 'r')
plt.legend()
plt.show()

outputs = network.activateOnDataset(testing_data)
for out, target in zip(outputs, testing_data['target']):
    print(f"output: {out}, target: {target}")

