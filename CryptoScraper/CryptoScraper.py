from bs4 import BeautifulSoup
from CryptoDict import getCryptoId
from datetime import datetime

def scrapeCurrency(soup):

    tag = soup.find("h1", class_ = "inlineblock")
    return tag.get_text().strip()


def scrapePrice(soup, crypto_curr):

    tag = soup.find("span", class_ = f"lastInst pid-{getCryptoId(crypto_curr)}-last")
    return tag.get_text().strip()


def scrapeVariation(soup, crypto_curr):

    tagVar = soup.find("i", class_ = f"pid-{getCryptoId(crypto_curr)}-pc")
    tagPerc = soup.find("i", class_ = f"pid-{getCryptoId(crypto_curr)}-pcp")
    return f"{tagVar.get_text().strip()} ({tagPerc.get_text().strip()})"


def getTimestamp(requestString):

    date = requestString.headers["Date"][:-4]
    timestamp = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S")
    return timestamp

    
