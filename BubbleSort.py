def BubbleSort(arr):

    for i in range(0,len(arr)-1):
        for j in range(i + 1,len(arr)):

            if arr[j] < arr[i]:

                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr



def main():

    arr = [1,23,5,2,5,7,64,45,8,7,5,89,0,9,8,9,7,8,4,6,78,77,7,78,5]
    
    print(BubbleSort(arr))

main()

