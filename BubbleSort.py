import numpy as np
import time

def BubbleSort(arr):

    for i in range(0,len(arr)-1):
        for j in range(i + 1,len(arr)):

            if arr[j] < arr[i]:

                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr



def main():

    start_time = time.time()

    arr = np.random.randint(1,1000,10000)
    
    print(BubbleSort(arr))

    print("--- %.5f segundos ---" % (time.time() - start_time))

main()

