from time import time
from concurrent.futures import ProcessPoolExecutor
from numpy import linspace


def sum_list(l):
    acc = 0
    for each in l:
        acc += each

    return acc


def mk_ranges(interval_list, amount):
    return [range(interval_list[i], interval_list[i + 1]) for i in range(amount)]


if __name__ == '__main__':

    start = time()

    intervals = [int(each) for each in list(linspace(0, 1800000000, 5))]
    range_list = mk_ranges(interval_list=intervals, amount=4)

    with ProcessPoolExecutor() as executor:
        futures = list()
        for r in executor.map(sum_list, range_list):
            futures.append(r)

        print("RESULT: {}".format(sum(futures)))
        print("TIME: {}".format(time() - start))
