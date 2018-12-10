import matplotlib.pyplot as plt
import numpy as np
import csv
import os

def plotIt(filename, extension):

    if extension == "txt":

        data = np.genfromtxt(f"{filename}.{extension}", delimiter = "|", usecols = (1))
        
    else:

        data = npgenfromtxt(f"{filename}.{extension}", delimiter = ",", usecols = (1))

    plt.plot(data, c = 'Red', ls = '--', marker = 'o', label = filename)
    plt.legend()
    plt.show()
