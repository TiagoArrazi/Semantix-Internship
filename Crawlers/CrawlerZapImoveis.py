#! /usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get 
from csv import writer
from os import stat
from datetime import datetime

for i in range(1, 11):

    url = ("https://www.zapimoveis.com.br/" +
          "aluguel/imoveis/" + 
          "#{\"pagina\":\"" + str(i) + "\",\"paginaOrigem\":\"Home\",\"formato\":\"Galeria\"}")

    requestString = get(url=url, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"})

    soup = BeautifulSoup(requestString.text, "html.parser")
    realties = soup.find_all("article", {"class":"minificha"}) #list of HTML-shaped realties info
    updates = soup.find_all("em", {"class":"atualizacao"}) #list of HTML-shaped info updates

    for k in range(0,len(realties)):

        try:
            realties[k] = eval(realties[k]['data-clickstream']) #turning 'data-clickstream' dictionary into an actual python dictionary
        except NameError:
            realties[k] = eval(realties[k]['data-clickstream']) #fix for an unknown bug 
            print("Error")

    for l in range(0,len(updates)):
        updates[l] = updates[l].get_text() #extracting text from updates

    res_csv = open("Residencial.csv", "a+")
    com_csv = open("Comercial.csv", "a+")
    rur_csv = open("Rural.csv", "a+")

    res_w = writer(res_csv, delimiter=";")
    com_w = writer(com_csv, delimiter=";")
    rur_w = writer(rur_csv, delimiter=";")

    print(realties)
    print(updates)

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

        date = datetime.strptime((requestString.headers["Date"][:-4]), "%a, %d %b %Y %H:%M:%S")

        if realties[j]['unitTypes'] == "Studio": #if the realty is a Studio, it will write in both Residential and Business files

            res_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'], 
                            realties[j]['areas'], realties[j]['bedrooms'], realties[j]['suites'], realties[j]['bathrooms'],
                            realties[j]['parkingSpaces'], realties[j]['rentalPrices'], realties[j]['condoFee'], realties[j]['iptuPrices'], 
                            realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2],
                            realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                            date, updates[j]])

            com_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'], 
                            realties[j]['areas'], realties[j]['bedrooms'], realties[j]['suites'], realties[j]['bathrooms'], 
                            realties[j]['parkingSpaces'], realties[j]['rentalPrices'], realties[j]['condoFee'], realties[j]['iptuPrices'], 
                            realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2], 
                            realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                            date, updates[j]])

            res_csv.flush()
            com_csv.flush()

            continue


        elif realties[j]['unitTypes'] in unitTypes_res: #if the realty type is in the residential realties list, 
                                         #redirects the writerow() to the Residential file
            res_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'], 
                            realties[j]['areas'], realties[j]['bedrooms'], realties[j]['suites'], realties[j]['bathrooms'], 
                            realties[j]['parkingSpaces'], realties[j]['rentalPrices'], realties[j]['condoFee'], realties[j]['iptuPrices'], 
                            realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2], 
                            realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                            date, updates[j]])

            res_csv.flush()


        elif realties[j]['unitTypes'] in unitTypes_com: #if the realty type is in the business realties list, 
                                         #redirects the writerow() to the Business file
            com_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'], 
                            realties[j]['areas'], realties[j]['bedrooms'], realties[j]['suites'], realties[j]['bathrooms'], 
                            realties[j]['parkingSpaces'], realties[j]['rentalPrices'], realties[j]['condoFee'], realties[j]['iptuPrices'], 
                            realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2], 
                            realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                            date, updates[i]])

            com_csv.flush()


        elif realties[j]['unitTypes'] in unitTypes_rur: #if the realty type is in the countryside realties list,
                                         #redirects the writerow() to the Countryside file
            rur_w.writerow([realties[j]['listingId'], realties[j]['unitTypes'], 
                            realties[j]['areas'], realties[j]['bedrooms'], realties[j]['suites'], realties[j]['bathrooms'], 
                            realties[j]['parkingSpaces'], realties[j]['rentalPrices'], realties[j]['condoFee'], realties[j]['iptuPrices'], 
                            realties[j]['address'][0],realties[j]['address'][1], realties[j]['address'][2], 
                            realties[j]['address'][3], realties[j]['address'][4], realties[j]['address'][5],
                            date, updates[j]])

            rur_csv.flush()
            
        res_csv.close()
        com_csv.close()
        rur_csv.close()



