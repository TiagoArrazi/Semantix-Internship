#! /usr/bin/env python3

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

# Dimensions of input arrays and goals
dataset = SupervisedDataSet(2, 1)

dataset.addSample([1, 1], [0])
dataset.addSample([1, 0], [1])
dataset.addSample([0, 1], [1])
dataset.addSample([0, 0], [0])

network = buildNetwork(dataset.indim, 4, dataset.outdim, bias=True)
# (dimensions of dataset input, amount of neurons in hidden layer, dimension of dataset output)
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.99)

for epoch in range(10000): #trains for 1000 epochs
    trainer.train()

# Alternate ways to train the network
# trainer.trainEpochs(1000)
# trainer.trainUntilConvergence()

test_data = SupervisedDataSet(2, 1)

test_data.addSample([1, 1], [0])
test_data.addSample([1, 0], [1])
test_data.addSample([0, 1], [1])
test_data.addSample([0, 0], [0])

trainer.testOnData(test_data, verbose=True)

