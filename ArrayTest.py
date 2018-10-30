import numpy as np

arr = np.loadtxt('sudokuState.txt', unpack = True).astype(int)

np.savetxt('newSudokuState.txt', arr, delimiter = '', fmt = '%4d')

arr = np.loadtxt('newSudokuState.txt', unpack = True).astype(int)

print(arr)
