#!/usr/bin/env python3                                                                     
                                                                                            #|
from sys import argv, exit                                                                  #|
from requests import get, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError  #|
from bs4 import BeautifulSoup                                                               #|
from time import sleep                                                                      #|
from csv import writer                                                                      #|
                                                                                            #|            
from CryptoScraper import *                                                                 #|
                                                                                            #|
#=============================================================================================

crypto_curr = argv[1]
url = f"https://m.investing.com/crypto/{crypto_curr}"

try:

    requestString = get(url = url, headers = {"User-Agent":"curl/7.52.1"})
    soup = BeautifulSoup(requestString.text, "lxml")

    print(scrapePrice(soup, crypto_curr).replace(',',''))
    print(scrapeVariation(soup, crypto_curr))
    print(getTimestamp(requestString))

    print('\n')

except (ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError):

    print("Couldn't connect, quitting!")
    exit()


save = input("Do you wish to save a file?(y/n) ")

if save == 'n':

    print("Okay, bye!")
    exit()

elif save == 'y':

    inputs = int(input("How many lines would like to register in the file? "))
    minutes = int(input("Amount of minutes between each registry? "))
    total_time = inputs * minutes

    print(f"This will take about {total_time} minute(s)")

    with open(f"{crypto_curr}-USD.csv","a+") as f:

        count = 0

        w = writer(f, delimiter=";")
        
        for i in range(0, inputs):

            requestString = get(url = url, headers = {"User-Agent":"curl/7.52.1"})
            soup = BeautifulSoup(requestString.text, "lxml")

            w.writerow([scrapePrice(soup, crypto_curr).replace(',',''), scrapeVariation(soup, crypto_curr), getTimestamp(requestString)])
            count += 1
            print(f"{count} line(s) inserted")

            sleep(60 * minutes)

    f.close()
    print("Done!")

else:

    print("Invalid argument, quitting!")
    exit()
