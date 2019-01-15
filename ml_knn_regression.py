#! /usr/bin/env python3

import math
import matplotlib.pyplot as plt
import numpy as np

class KNNRegression:
    def __init__(self, x, y, k=3):
        self.n_samples = len(x)
        self.n_attrbs = len(x[0])
        self.x, self.y, self.k = x, y, k

    def predict(self, sample):
        d = dict()
        for i in range(self.n_samples):
            _sum = 0
            for j in range(self.n_attrbs):
                _sum += math.pow(sample[j] - self.x[i][j], 2)
            d[i] = math.sqrt(_sum)
        k_neighbors = sorted(d, key=d.get)[:self.k]
        _sum = sum([self.y[index] for index in k_neighbors])
        return _sum / self.k

if __name__ == '__main__':
    inputs = [[2, 50], [4, 90], [1, 38], [5, 105], [2, 48],
              [6, 120], [3, 65], [4, 80], [5, 100], [3, 60]]

    outputs = [250, 490, 138, 505, 248, 612, 365, 470, 500, 360]

    knn = KNNRegression(inputs, outputs)
    results = []
    for _input in inputs:
        results.append(knn.predict(_input))

    plt.plot(np.linspace(-1, 1, 10), 
             outputs, 
             label='expected', 
             color='black',
             linewidth=1.5)

    plt.plot(np.linspace(-1, 1, 10), 
             results, 
             label='expected', 
             color='red',
             linewidth=1.5)

    plt.show()
