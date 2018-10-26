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

    arr = [12,34,2,1,3,4,2,2,22,65,1,4,44,2,4,4,213,2,34,22,3,14,343,24,24,7,3742,4,24,777,4234,2,4,414,99,5656,867,8,9]

    MergeSort(arr, 0, len(arr) - 1)

    print(arr)

main()

