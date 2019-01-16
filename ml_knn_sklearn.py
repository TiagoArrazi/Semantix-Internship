#! /usr/bin/env python3

from sklearn.neighbors import KNeighborsClassifier


inputs, outputs = list(), list()

with open('haberman_dataset.txt', 'r') as f:
    for line in f.readlines():
        attrb = line.replace('\n','').split(',')
        inputs.append([int(attrb[0]), int(attrb[2])])
        outputs.append(int(attrb[3]))
                
perc = 0.6
limit = int(perc * len(inputs))

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(inputs[:limit], outputs[:limit])
labels = knn.predict(inputs[limit:])
correct, label_index = 0, 0

for i in range(limit, len(inputs)):
    if labels[label_index] == outputs[i]:
        correct += 1
    label_index += 1

print(f'Training: {limit}')
print(f'Tests: {len(inputs) - limit}')
print(f'Correct answers: {correct}')
print(f'Accuracy: {((100 * correct) / (len(inputs) - limit)):.2f}%')
