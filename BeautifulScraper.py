from bs4 import BeautifulSoup
import requests
import Scraper

def beautifulCotationScraper(soup):

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

    requestString = requests.get(url = myURL, headers = {'User-Agent':'curl/7.52.1'})
    soup = BeautifulSoup(requestString.text, "lxml")

    print(beautifulCotationScraper(soup))
    print(beautifulCurrencyScraper(soup))
    print(beautifulVariationScraper(soup))
    print(Scraper.scrapeTimestamp(requestString))


    



