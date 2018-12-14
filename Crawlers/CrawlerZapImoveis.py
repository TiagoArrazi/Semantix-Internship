#! /usr/bin/env python3

from selenium import webdriver

from bs4 import BeautifulSoup
from requests import get

from csv import writer
from os import stat
from datetime import datetime
from time import sleep

OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument("--headless")
OPTIONS.add_argument("""--user-agent=Mozilla/5.0 
                                     (X11; Linux x86_64) 
                                     AppleWebKit/537.36 
                                     (KHTML, like Gecko) 
                                     Chrome/47.0.2526.80 
                                     Safari/537.36""")

null = None
driver = webdriver.Chrome(chrome_options=OPTIONS)
URL = """https://www.zapimoveis.com.br/aluguel/imoveis/#{%22pagina%22:%221%22}"""
HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
driver.get(URL)

while(1):

    print(driver.current_url)
    response = get(url=driver.current_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    realties = soup.find_all("article", {"class":"minificha"}) #list of HTML-shaped realties info

    if len(realties) == 0:
        print("Done!")
        break

    else:

        updates = soup.find_all("em", {"class":"atualizacao"}) #list of HTML-shaped info updates

        for k in range(0,len(realties)):

            try:

                realties[k] = eval(realties[k]['data-clickstream']) #turning 'data-clickstream' dictionary into an actual python dictionary
                key_list = list(realties[k].keys())

                for key in key_list:

                    if isinstance(realties[k][key], list):
                        if len(realties[k][key]) == 0:
                            realties[k][key] = '0'

            except NameError:
   
                print("Error")
                realties[k] = eval(realties[k]['data-clickstream']) #fix for an unknown bug 
                key_list = list(realties[k].keys())

                for key in key_list:
    
                    if isinstance(realties[k][key], list):
                        if len(realties[k][key]) == 0:
                            realties[k][key] = '0'

            print(realties[k]['listingId'])
        print('--------')
        for l in range(0,len(updates)):
            updates[l] = updates[l].get_text() #extracting text from updates

        res_csv = open("Residencial.csv", "a+")
        com_csv = open("Comercial.csv", "a+")
        rur_csv = open("Rural.csv", "a+")

        res_w = writer(res_csv, delimiter=";")
        com_w = writer(com_csv, delimiter=";")
        rur_w = writer(rur_csv, delimiter=";")

        if stat("Residencial.csv").st_size == 0: #checks file size, creates header if empty(st_size==0)
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


        unitTypes_res = ["Apartamento Padrão","Casa de Condomínio", #possible residential realties, according to the website
                         "Casa de Vila","Casa Padrão","Cobertura",
                         "Flat","Kitchenette/Conjugados","Loft",
                         "Loteamento/Condomínio","Studio","Terreno Padrão"]

        unitTypes_com = ["Box/Garagem","Casa Comercial", #possible business realties
                         "Conjunto Comercial/Sala","Galpão/Depósito/Armazém",
                         "Hotel","Indústria","Loja Shopping/ Ct Comercial",
                         "Loja/Salão","Motel","Pousada/Chalé","Prédio Inteiro","Studio"]

        unitTypes_rur = ["Chácara","Fazenda","Sítio"] #possible countryside realties

        for j in range(0, len(realties)):

            date = datetime.strptime((response.headers["Date"][:-4]), "%a, %d %b %Y %H:%M:%S")

            if realties[j]['unitTypes'][0] == "Studio": #if the realty is a Studio, it will write in both Residential and Business files

                res_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'][0], 
                                realties[j]['areas'][0], realties[j]['bedrooms'][0], realties[j]['suites'][0], realties[j]['bathrooms'],
                                realties[j]['parkingSpaces'][0], realties[j]['rentalPrices'][0], 
                                realties[j]['condoFee'], realties[j]['iptuPrices'][0], 
                                realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2],
                                realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                                date, updates[j]])

                com_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'][0], 
                                realties[j]['areas'][0], realties[j]['bedrooms'][0], realties[j]['suites'][0], realties[j]['bathrooms'], 
                                realties[j]['parkingSpaces'][0], realties[j]['rentalPrices'][0],
                                realties[j]['condoFee'], realties[j]['iptuPrices'][0], 
                                realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2], 
                                realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                                date, updates[j]])

                res_csv.flush() 
                com_csv.flush()

                continue


            elif realties[j]['unitTypes'][0] in unitTypes_res: #if the realty type is in the residential realties list, 
                                                               #redirects the writerow() to 'Residencial.csv'
                res_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'][0],
                                realties[j]['areas'][0], realties[j]['bedrooms'][0], realties[j]['suites'][0], realties[j]['bathrooms'],
                                realties[j]['parkingSpaces'][0], realties[j]['rentalPrices'][0], 
                                realties[j]['condoFee'], realties[j]['iptuPrices'][0],
                                realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2],
                                realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                                date, updates[j]])

                res_csv.flush()


            elif realties[j]['unitTypes'][0] in unitTypes_com: #if the realty type is in the business realties list, 
                                                               #redirects the writerow() to 'Comercial.csv'
                com_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'][0],
                                realties[j]['areas'][0], realties[j]['bedrooms'][0], realties[j]['suites'][0], realties[j]['bathrooms'],
                                realties[j]['parkingSpaces'][0], realties[j]['rentalPrices'][0], 
                                realties[j]['condoFee'], realties[j]['iptuPrices'][0],
                                realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2],
                                realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                                date, updates[j]])

                com_csv.flush()


            elif realties[j]['unitTypes'][0] in unitTypes_rur: #if the realty type is in the countryside realties list,
                                                               #redirects the writerow() to 'Rural.csv'
                rur_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'][0],
                                realties[j]['areas'][0], realties[j]['bedrooms'][0], realties[j]['suites'][0], realties[j]['bathrooms'],
                                realties[j]['parkingSpaces'][0], realties[j]['rentalPrices'][0], 
                                realties[j]['condoFee'], realties[j]['iptuPrices'][0],
                                realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2],
                                realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                                date, updates[j]])

                rur_csv.flush()
            
        res_csv.close()
        com_csv.close()
        rur_csv.close()

        driver.execute_script("document.getElementById('proximaPagina').click()")
        sleep(5)
