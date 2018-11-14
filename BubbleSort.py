#!/usr/bin/env python3

import numpy as np #to generate random array
import time #to keep track of runtime

def BubbleSort(arr):

    for i in range(0,len(arr)-1): #iterates through the array starting from the very beginning
        for j in range(i + 1,len(arr)): #always 1 step ahead of index i

            if arr[j] < arr[i]: #value comparison

                temp = arr[i] #if the value in index i is bigger than the one in index j, temp temporarily stores arr[i]
                arr[i] = arr[j] #value substitution
                arr[j] = temp #the values of arr[i] and arr[j] have switched

    return arr #returns the sorted array



def main():

    start_time = time.time() #starting time

    arr = np.random.randint(1,1000,10000) #generates random array with 10000 values from 1 to 1000
    
    print(BubbleSort(arr)) #sort the generated array

    print("--- %.5f seconds ---" % (time.time() - start_time)) #calculates time delta to get runtime 

main()

