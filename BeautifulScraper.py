#!/usr/bin/env python3

from bs4 import BeautifulSoup #Scraping specific library
import requests
import Scraper #module to reuse getTimestamp() method
import csv
import os

def beautifulPriceScraper(soup):

    tag = soup.find("span", class_ = "pid-2103-last") #searches for <span> by class name "pid-2103-last"
    return tag.get_text().strip() #returns the tag content without blank spaces
    
    
def beautifulCurrencyScraper(soup):

    tag = soup.find("h1", class_ = "instrumentH1inlineblock") #searches for <h1> by class name "instrumentH1inlineblock" 
    return tag.get_text().strip() #returns the tag content without blank spaces


def beautifulVariationScraper(soup):

    tagVar = soup.find("i", class_ = "greenFont pid-2103-pc") #searches for <i> by class name "greenFont pid-2103-pc"
    tagPerc = soup.find("i", class_ = "parentheses greenFont pid-2103-pcp") #searches for <i> by class name "greenFont pid-2103-pcp"
    return f"{tagVar.get_text().strip()} ({tagPerc.get_text().strip()})" #returns both tags content concatenated into 1 string without blank spaces


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

