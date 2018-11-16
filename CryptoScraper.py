#! /usr/bin/env python3

from requests import get
from datetime import datetime
import os
from csv import writer
from bs4 import BeautifulSoup

def scrape(soup, i):

    tag = soup.findAll("tr")
    return f"{tag[i].get_text().strip()}"


url = "https://m.investing.com/crypto"

requestString = get(url = url, headers = {"User-Agent":"curl 7.52.1"})
soup = BeautifulSoup(requestString.text, "lxml")

for i in range(0,10):

    print(scrape(soup,i))
    print("\n")
