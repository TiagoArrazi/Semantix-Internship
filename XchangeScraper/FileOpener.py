import csv
from requests import get
from time import sleep
from bs4 import BeautifulSoup
from XCHBeautifulScraper import *
import os
from Plotter import plotIt

def makeFile(url, currCombination, currSoup):

    extension = input("File extension (without the \".\"): ")
    inserts = input("Amount of registries: ")
    minutes = input("Time interval between each scraping: ")

    tmpFilename = beautifulCurrencyScraper(currSoup).split()
    filename = f"{tmpFilename[2]} {tmpFilename[3]}_{tmpFilename[4]} {tmpFilename[5]}"
    processTime = int(minutes) * int(inserts)


    if extension == "txt":

        print(f"This will take about {processTime} minutes")

        f = open(f"{filename}.{extension}", "a+")
            
        for i in range(1,int(inserts) + 1):

            requestString = get(url = url, headers = {'User-Agent':'curl/7.52.1'})
            soup = BeautifulSoup(requestString.text, "lxml")

            f.write(f"{beautifulPriceScraper(soup, currCombination)} | {beautifulVariationScraper(soup, currCombination)} | {getTimestamp(requestString)} \n")
            
            sleep(60 * int(minutes))

        print("Done!")
        plotItInput = input("Do you want to plot it?(y/n) ")

        if plotItInput == "y":

            plotIt(filename, extension)

        elif plotItInput == "n":

            print("Goodbye!")
            sys.exit()

        else:

            print("I guess you don't want to plot it, bye!")

        f.close()


    elif extension == "csv":

        print(f"This will take about {processTime} minutes")

        f = open(f"{filename}.{extension}", "a+")
        w = csv.writer(f, delimiter = ";")

        for i in range(1, int(inserts) + 1):

            requestString = get(url = url, headers = {'User-Agent':'curl/7.52.1'})
            soup = BeautifulSoup(requestString.text, "lxml")

            w.writerow([beautifulCurrencyScraper(soup), beautifulPriceScraper(soup, currCombination), beautifulVariationScraper(soup, currCombination), getTimestamp(requestString)])

            sleep(60 * int(minutes))

        f.close()
        print("Done")

    else:

        print("The only valid formats are .txt and .csv")



