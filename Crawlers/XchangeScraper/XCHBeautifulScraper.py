import Dictionaries
import datetime

def beautifulPriceScraper(soup, currCombination):

    tag = soup.find("span", class_ = f"pid-{Dictionaries.getCombinationID(currCombination)}-last")
    return tag.get_text().strip()


def beautifulCurrencyScraper(soup):

    tag = soup.find("h1", class_ = "instrumentH1inlineblock")
    return tag.get_text().strip()


def beautifulVariationScraper(soup, currCombination):

    tagVar = soup.find("i", class_ = f"pid-{Dictionaries.getCombinationID(currCombination)}-pc")
    tagPerc = soup.find("i", class_ = f"pid-{Dictionaries.getCombinationID(currCombination)}-pcp")
    return f"{tagVar.get_text().strip()} ({tagPerc.get_text().strip()})"

def getTimestamp(requestString):

    date = requestString.headers["Date"][:-4]
    timestamp = datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S")
    return timestamp
