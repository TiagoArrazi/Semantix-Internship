#!/usr/bin/env python3

import numpy as np

arr = np.loadtxt('sudokuState.txt', unpack = True).astype(int) #loads .txt file to array

np.savetxt('newSudokuState.txt', arr, delimiter = '', fmt = '%4d') #saves array into .txt file

arr = np.loadtxt('newSudokuState.txt', unpack = True).astype(int)

print(arr)
