#! /usr/bin/env python3

# Iris-setosa: 0
# Iris-versicolor: 1
# Iris-virginica: 2
 

import numpy as np

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

inputs = np.genfromtxt('ModifiedIrisDataset.txt', delimiter=',', usecols=(0,1,2,3))
outputs = np.genfromtxt('ModifiedIrisDataset.txt', delimiter=',', usecols=(4))

training_inputs = np.concatenate((inputs[:35], inputs[50:85], inputs[100:135]))
training_outputs = np.concatenate((outputs[:35], outputs[50:85], outputs[100:135]))

testing_inputs = np.concatenate((inputs[35:50], inputs[85:100], inputs[135:]))
testing_outputs = np.concatenate((outputs[35:50], outputs[85:100], outputs[135:]))

training_dataset = SupervisedDataSet(4, 1)
for input_sample, output_sample in zip(training_inputs, training_outputs):
    training_dataset.addSample(input_sample, output_sample)

network = buildNetwork(training_dataset.indim, 2, training_dataset.outdim, bias=True)
trainer = BackpropTrainer(network, training_dataset, learningrate=0.01, momentum=0.3)

trainer.trainEpochs(10000)

test = SupervisedDataSet(4, 1)
for testing_input, testing_output in zip(testing_inputs, testing_outputs):
    test.addSample(testing_input, testing_output)

trainer.testOnData(test, verbose=True)
