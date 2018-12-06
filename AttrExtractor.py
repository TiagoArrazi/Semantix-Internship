from bs4 import BeautifulSoup
from requests import get

requestString = get(url="https://www.zapimoveis.com.br/aluguel/imoveis/#{%22pagina%22:%221%22,%22paginaOrigem%22:%22Home%22,%22formato%22:%22Lista%22}", headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"})

soup = BeautifulSoup(requestString.text, "html.parser")
element = soup.find_all("article" , {"class":"minificha"})

print(eval(element[0]['data-clickstream']))
    

