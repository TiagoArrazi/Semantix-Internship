#!/usr/bin/env python3

from requests import get
from datetime import datetime
from csv import writer
from os import stat
from bs4 import BeautifulSoup

myURL = "https://m.investing.com/currencies/usd-brl"

#-----------------------------------------------------------

def scrapePrice(soup):

    tag = soup.find("span", class_ = "pid-2103-last")
    return tag.get_text().strip()

#-----------------------------------------------------------

def scrapeCurrency(soup):

    tag = soup.find("h1", class_ = "instrumentH1inlineblock")
    return tag.get_text().strip()

#-----------------------------------------------------------

def scrapeVariation(soup):

    tag = soup.find("i", class_ = "pid-2103-pc")
    return tag.get_text().strip()

#-----------------------------------------------------------

def scrapePercentual(soup):
    
    tag = soup.find("i", class_ = "pid-2103-pcp")
    return tag.get_text().strip()

#-----------------------------------------------------------

def scrapeTimestamp(request):

    date = request.headers["Date"][:-4]
    timestamp = datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S")

    return timestamp

#-----------------------------------------------------------

if __name__ == "__main__":
    
    requestString = get(url = myURL, headers = {'User-Agent':'curl/7.52.1'})
    soup = BeautifulSoup(requestString.text, "html.parser")

    f = open("/home/ec2-user/Registros/Tiago/Dolar.csv", "a+")

    w = writer(f, delimiter = ";")

    if stat("/home/ec2-user/Registros/Tiago/Dolar.csv").st_size == 0:
        w.writerow(["Moeda", "Cotacao", "Variacao", "Timestamp"])

    w.writerow([scrapeCurrency(soup),scrapePrice(soup),scrapeVariation(soup),scrapePercentual(soup),scrapeTimestamp(requestString)])
    
    f.close()














