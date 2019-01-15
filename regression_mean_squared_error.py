#! /usr/bin/env python3


from sklearn.metrics import mean_squared_error


y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
print(mean_squared_error(y_true, y_pred))

y_true = [1, 2, 3]
y_pred = [1, 2, 3]
print(mean_squared_error(y_true, y_pred))

y_true = [1, 2, 3]
y_pred = [10, 20, 30]
print(mean_squared_error(y_true, y_pred))

