#! /usr/bin/env python3

# Classification with PyBrain - 3D XOR

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

dataset = SupervisedDataSet(3, 1)
dataset.addSample([0, 0, 0], [0])
dataset.addSample([0, 0, 1], [1])
dataset.addSample([0, 1, 0], [1])
dataset.addSample([0, 1, 1], [0])
dataset.addSample([1, 0, 0], [1])
dataset.addSample([1, 0, 1], [0])
dataset.addSample([1, 1, 0], [0])
ataset.addSample([1, 1, 1], [1])

network = buildNetwork(dataset.indim, 6, 6, dataset.outdim, bias=True)
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.9)
trainer.trainEpochs(10000)

test = SupervisedDataSet(3, 1)
test.addSample([0, 0, 0], [0])
test.addSample([0, 0, 1], [1])
test.addSample([0, 1, 0], [1])
test.addSample([0, 1, 1], [0])
test.addSample([1, 0, 0], [1])
test.addSample([1, 0, 1], [0])
test.addSample([1, 1, 0], [0])
test.addSample([1, 1, 1], [1])

trainer.testOnData(test, verbose=True)
