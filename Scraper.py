import requests as rq
import datetime
import csv
import time

myURL = "https://m.investing.com/currencies/usd-brl"

def scrapeCotation(requestString):

    indexInit = requestString.find("pid-2103-last") + 32
    indexFinal = indexInit + 7
    cotString = requestString[indexInit:indexFinal].strip()

    return cotString


def scrapeCurrency(requestString):

    indexInit = requestString.find("instrumentH1inlineblock") + 30
    indexFinal = indexInit + 31
    currString = requestString[indexInit:indexFinal].strip()

    return currString


def scrapeVariation(requestString):

    indexInit = requestString.find("greenFont pid-2103-pc") + 44
    indexFinal = indexInit + 7
    varString = requestString[indexInit:indexFinal].strip()

    indexInit = requestString.find("parentheses greenFont pid-2103-pcp") + 56
    indexFinal = indexInit + 7
    percString = requestString[indexInit:indexFinal].strip()

    return f"{varString} ({percString})"

def scrapeTimestamp(request):

    date = request.headers["Date"][:-4]
    timestamp = datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S")

    return timestamp


if __name__ == "__main__":

    with open("Exchange.csv", "w") as f:

        XCH_writer = csv.writer(f, delimiter = ";")
        XCH_writer.writerow(["Moeda", "Cotacao", "Variacao", "Timestamp"])

        for i in range(0, 100):

            requestString = rq.get(url = myURL, headers = {'User-Agent':'curl/7.52.1'})
            XCH_writer.writerow([scrapeCurrency(requestString.text), scrapeCotation(requestString.text), scrapeVariation(requestString.text), 
                                scrapeTimestamp(requestString)])

            time.sleep(10)












