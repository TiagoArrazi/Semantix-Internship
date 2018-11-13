#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import Scraper
import time
import csv
import os

def beautifulPriceScraper(soup):

    tag = soup.find("span", class_ = "pid-2103-last")
    return tag.get_text().strip()
    
    
def beautifulCurrencyScraper(soup):

    tag = soup.find("h1", class_ = "instrumentH1inlineblock")
    return tag.get_text().strip()


def beautifulVariationScraper(soup):

    tagVar = soup.find("i", class_ = "greenFont pid-2103-pc")
    tagPerc = soup.find("i", class_ = "parentheses greenFont pid-2103-pcp")
    return f"{tagVar.get_text().strip()} ({tagPerc.get_text().strip()})"


if __name__ == "__main__":

    myURL = "https://m.investing.com/currencies/usd-brl"

    try:

        requestString =  requests.get(url = myURL, headers = {'User-Agent':'curl/7.52.1'})
        soup = BeautifulSoup(requestString.text, "lxml")

        XCH_writer.writerow()

    except ConnectionError: 

         """Couldn't connect  :(
            Verify your internet connection and try again  ;)"""
    

    f.close()

