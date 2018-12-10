#! /usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get 
from collections import defaultdict

url = """https://www.zapimoveis.com.br/aluguel/imoveis/#{
      \"pagina\":\"1\",
      \"paginaOrigem\":\"Home\",
      \"formato\":\"Lista\"}"""

requestString = get(url=url, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"""})

soup = BeautifulSoup(requestString.text, "html.parser")
realties = soup.find_all("article", {"class":"minificha"})
dict_master = defaultdict(dict)
id_list = list()


for realty in realties:

    try:

        realty_dict = eval(realty['data-clickstream'])
        print(realty_dict['unitTypes'])

    except NameError:

        print(realty_dict['unitTypes'])
        #print("Error")
        
    

    




