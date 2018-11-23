#! /usr/bin/env python3

from os import stat
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, get

crypto_Url = "https://m.investing.com/crypto/"

requestString = get(url = crypto_Url, headers = {'User-Agent':'curl/7.52.1'})
soup = BeautifulSoup(requestString.text, "lxml")
content = soup.findAll('tr')
date = datetime.strptime(requestString.headers['Date'][:-4], '%a, %d %b %Y %H:%M:%S')

f = open("Registro.csv", "a+")
w = writer(f, delimiter = ";")

if stat("Registro.csv").st_size == 0:
    w.writerow(["#", "Nome", "Preco(USD)", "Var(24H)", "Var(7D)", "Simbolo", "Preco(BTC)", "Valor de Mercado", "Vol(24H)", "Vol Total"])

for c in content[1:]:

    l = c.get_text().replace('\t', '').split('\n')
    L = list(filter(None, l))

    w.writerow([L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9]])


