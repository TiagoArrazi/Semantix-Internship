import numpy as np
import time

def Merge(arr, b, m, e):

    n1 = m - b + 1 # 1st subarray size
    n2 = e - m # 2nd subarray size

    L_Array = [0] * (n1)
    R_Array = [0] * (n2)

    for i in range(0,n1):
        L_Array[i] = arr[b + i] # Copying to subarray

    for j in range(0,n2):
        R_Array[j] = arr[m + 1 + j] # Copying to subarray

    i = 0
    j = 0
    k = b

    while i < n1 and j < n2:

        if L_Array[i] <= R_Array[j]:

            arr[k] = L_Array[i]
            i += 1

        else:

            arr[k] = R_Array[j]
            j += 1

        k += 1

    while i < n1:

        arr[k] = L_Array[i]
        i += 1
        k += 1

    while j < n2:

        arr[k] = R_Array[j]
        j += 1
        k += 1

def MergeSort(arr, b, e):

    m = (b + (e - 1)) // 2

    if b < e:

        MergeSort(arr, b, m)
        MergeSort(arr, m+1, e)
        Merge(arr, b, m, e)


   

def main():

    start_time = time.time()

    arr = np.random.randint(1,1000,10000)

    MergeSort(arr, 0, len(arr) - 1)

    print(arr)

    print("--- %.5f segundos ---" % (time.time() - start_time))
   
main()

