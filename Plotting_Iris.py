import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('IrisDataset.txt', delimiter = ',', usecols = (0,1,2,3))

plt.plot(data[:50,0], c = 'Red', ls = ' ', marker = 'o', label = 'Iris-Setosa Sepal Length')
plt.plot(data[50:100,0], c = 'Blue', ls = ' ', marker = 'o', label = 'Iris-Versicolor Sepal Length')
plt.plot(data[100:150,0], c = 'Green', ls = ' ', marker = 'o', label = 'Iris-Virginica Sepal Length')
plt.legend()
plt.show()

plt.plot(data[:50,1], c = 'Red', ls = ' ', marker = 'o', label = 'Iris-Setosa Sepal Width')
plt.plot(data[50:100,1], c = 'Blue', ls = ' ', marker = 'o', label = 'Iris-Versicolor Sepal Width')
plt.plot(data[100:150,1], c = 'Green', ls = ' ', marker = 'o', label = 'Iris-Virginica Sepal Width')
plt.legend()
plt.show()

plt.plot(data[:50,2], c = 'Red', ls = ' ', marker = 'o', label = 'Iris-Setosa Petal Length')
plt.plot(data[50:100,2], c = 'Blue', ls = ' ', marker = 'o', label = 'Iris-Versicolor Petal Length')
plt.plot(data[100:150,2], c = 'Green', ls = ' ', marker = 'o', label = 'Iris-Virginica Petal Length')
plt.legend()
plt.show()

plt.plot(data[:50,3], c = 'Red', ls = ' ', marker = 'o', label = 'Iris-Setosa Petal Width')
plt.plot(data[50:100,3], c = 'Blue', ls = ' ', marker = 'o', label = 'Iris-Versicolor Petal Width')
plt.plot(data[100:150,3], c = 'Green', ls = ' ', marker = 'o', label = 'Iris-Virginica Petal Width')
plt.legend(loc = 'upper right')
plt.show()

