from time import time


start = time()
acc = 0

for i in range(1800000000):
    acc += i

print("RESULT = {}".format(acc))
print("TIME = {}".format(time() - start))