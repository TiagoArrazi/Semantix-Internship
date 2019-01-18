#! /usr/bin/env python3

from random import random

class Perceptron:
    def __init__(self, samples, outputs, learning_rate=0.1, epochs=1000, threshold=-1):
        self.samples = samples
        self.outputs = outputs
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.threshold = threshold
        self.n_samples = len(samples)
        self.n_attrbs = len(samples[0])
        self.weights = list()

    def fit(self):
        for sample in self.samples:
            sample.insert(0, -1)

        for i in range(self.n_attrbs):
            self.weights.append(random())

        self.weights.insert(0, self.threshold)
        n_epochs = 0 # epochs counter

        while True:
            error = False # error does not exist initially

            for i in range(self.n_samples):
                u = 0
                for j in range(self.n_attrbs + 1):
                    u += self.weights[j] * self.samples[i][j]
                y = self.signal(u)

                if y != self.outputs[i]:
                    aux_error = self.outputs[i] - y

                    for j in range(self.n_attrbs + 1):
                        self.weights[j] = self.weights[j] + self.learning_rate * aux_error * self.samples[i][j]

                error = True # error still exists

            n_epochs += 1

            if not error or n_epochs > self.epochs:
                break

    def test(self, sample):
        sample.insert(0, -1)
        u = 0
        for i in range(self.n_attrbs + 1):
            u += self.weights[i] * sample[i]
        y = self.signal(u)
        print(f'{sample[1:]} -> {y}')

    def signal(self, u):
        if u >= 0:
            return 1
        return -1


samples_inputs = [[0.72, 0.82], [0.91, -0.69],
	          [0.46, 0.80],   [0.03, 0.93],
	          [0.12, 0.25],   [0.96, 0.47],
	          [0.8, -0.75],   [0.46, 0.98],
	          [0.66, 0.24],   [0.72, -0.15],
                  [0.35, 0.01],   [-0.16, 0.84],
  	          [-0.04, 0.68],  [-0.11, 0.1],
	          [0.31, -0.96],   [0.0, -0.26],
	          [-0.43, -0.65],  [0.57, -0.97],
	          [-0.47, -0.03],  [-0.72, -0.64],
	          [-0.57, 0.15],   [-0.25, -0.43],
	          [0.47, -0.88],   [-0.12, -0.9],
	          [-0.58, 0.62],   [-0.48, 0.05],
	          [-0.79, -0.92],  [-0.42, -0.09],
	          [-0.76, 0.65],   [-0.77, -0.76]]

samples_outputs = [-1, -1, -1, -1, -1, -1, -1, -1,
	           -1, -1, -1, -1, -1, 1, 1, 1, 1,
	            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

network = Perceptron(samples_inputs, samples_outputs)
network.fit()

network.test([0.72, 0.82])
network.test([-0.77, -0.76])
# Unkown situations
network.test([0.54, -0.43])
network.test([0.0, 0.0])
