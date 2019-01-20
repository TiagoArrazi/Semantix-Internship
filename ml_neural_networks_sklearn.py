#! /usr/bin/env python3

from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X, y = iris.data, iris.target

mlp = MLPClassifier(solver='adam', alpha=0.0001, hidden_layer_sizes=(5,), random_state=1,
                    learning_rate='constant', learning_rate_init=0.01, max_iter=500, 
                    activation='logistic', momentum=0.9, verbose=True, tol=0.0001)

X_training, X_testing, y_training, y_testing = train_test_split(X, y, test_size=0.3, 
                                                                random_state=1)

mlp.fit(X_training, y_training)
outputs = mlp.predict(X_testing)

print('----------------------------------------------')

print('Network output: {}'.format(outputs))
print('Expected output: {}'.format(y_testing))

print('----------------------------------------------')

print('Score: {}'.format(mlp.score(X_testing, y_testing)))
