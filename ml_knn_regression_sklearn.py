#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split



k = 9
boston = load_boston()
knn = KNeighborsRegressor(n_neighbors=k)
x, y = boston.data[:50], boston.target[:50]
y_ = knn.fit(x, y).predict(x)
plt.plot(np.linspace(-1, 1, 50), y, label='data', color='black')
plt.plot(np.linspace(-1, 1, 50), y_, label='prediction', color='red')
plt.legend()
plt.show()

