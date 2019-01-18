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


samples_inputs = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2],
                  [0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]
samples_outputs = [1, -1, -1, 1]
network = Perceptron(samples_inputs, samples_outputs)
network.fit()

network.test([0.1, 0.4, 0.7])
network.test([0.3, 0.7, 0.2])
network.test([0.6, 0.9, 0.8])
network.test([0.5, 0.7, 0.1])
