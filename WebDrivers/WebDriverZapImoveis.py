#! /usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get 
from collections import defaultdict
from csv import writer
from os import stat

url = """https://www.zapimoveis.com.br/aluguel/imoveis/#{
      \"pagina\":\"1\",
      \"paginaOrigem\":\"Home\",
      \"formato\":\"Lista\"}"""

requestString = get(url=url, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"})

soup = BeautifulSoup(requestString.text, "html.parser")
realties = soup.find_all("article", {"class":"minificha"}) #list of HTML-shaped realties info
updates = soup.find_all("em", {"class":"atualizacao"}) #list of HTML-shaped info updates

for i in range(0,len(realties)):

    try:
        realties[i] = eval(realties[i]['data-clickstream']) #turning 'data-clickstream' dictionary into an actual python dictionary
    except NameError:
        realties[i] = eval(realties[i]['data-clickstream']) #fix for an unknown bug 
        print("Error")

for i in range(0,len(updates)):
    updates[i] = updates[i].get_text() #extracting text from updates

res_csv = open("Residencial.csv", "a+")
com_csv = open("Comercial.csv", "a+")
rur_csv = open("Rural", "a+")

res_w = writer(res_csv, delimiter=";")
com_w = writer(com_csv, delimiter=";")
rur_w = writer(rur_csv, delimiter=";")

if stat("Residencial.csv").st_size == 0:
    res_w.writerow(["ID","Subtipo","Area",
                    "Quartos","Suites","Banheiros","Vagas",
                    "Preco Aluguel","Preco Cond.","Preco IPTU",
                    "Pais","Estado","Cidade","Bairro","Rua","Numero"])

if stat("Comercial.csv").st_size == 0:
    com_w.writerow(["ID","Subtipo","Area",
                    "Quartos","Suites","Banheiros","Vagas",
                    "Preco Aluguel","Preco Cond.","Preco IPTU",
                    "Pais","Estado","Cidade","Bairro","Rua","Numero"])

if stat("Rural.csv").st_size == 0:
    rur_w.writerow(["ID","Subtipo","Area",
                    "Quartos","Suites","Banheiros","Vagas",
                    "Preco Aluguel","Preco Cond.","Preco IPTU",
                    "Pais","Estado","Cidade","Bairro","Rua","Numero"])


unitTypes_res = ["","","","","","","","","","",""]
unitTypes_com = ["","","","","","","","","","","",""]
unitTypes_rur = ["","",""]

'''
if unitTypes == "Studio":
    res_w.writerow()
    com_w.writerow()
    continue

elif unitTypes in unitTypes_res:
    res_w.writerow()

elif unitTypes in unitTypes_com:
    com_w.writerow()

elif unitTypes in unitTypes_rur:
    rur_w.writerow()
'''


