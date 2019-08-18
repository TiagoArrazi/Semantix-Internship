from time import time

start = time()
acc = 0
for each in range(1800000000):
    acc += each

print("RESULT: {}".format(acc))
print("TIME: {}".format(time() - start))