#!/usr/bin/env python3

#Acceptable initial inputs-> (currency_1) (currency_2) (amount_of_requests)
#                            (currency_1) (currency_2) ("file"<-to save results in a file) 

#Lib imports
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, get
import sys
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from time import sleep
from math import trunc

#Module imports
from XCHBeautifulScraper import *
from FileOpener import *

currCombination = f"{sys.argv[1]}-{sys.argv[2]}"
xchURL = f"https://m.investing.com/currencies/{currCombination}"

try:

    requestString = get(url = xchURL, headers = {'User-Agent':'curl/7.52.1'})
    soup = BeautifulSoup(requestString.text, "html.parser")

except (ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError):

    print("Couldn't connect, quitting!")
    sys.exit()

if len(sys.argv) == 4:

    if sys.argv[3] == "file"l

       makeFile(xchURL, currCombination, soup)

    else:

        minutes = input("Time interval between each scraping (minutes): ")
        print("\n")

        for i in range(0,int(sys.argv[3])):

            requestString = get(url = xchURL, headers = {'User-Agent':'curl/7.52.1'})
            soup = BeautifulSoup(requestString.text, "html.parser")

            print(beautifulCurrencyScraper(soup))
            print(beautifulPriceScraper(soup, currCombination))
            print(beautifulVariationScraper(soup, currCombination))
            print(getTimestamp(requestString))
            print("\n")

            sleep(60 * float(minutes))

        print("Done!")

else:

    print(beautifulCurrencyScraper(soup))
    print(beautifulPriceScraper(soup, currCombination))
    print(beautifulVariationScraper(soup, currCombination))
    print(getTimestamp(requestString))
    
