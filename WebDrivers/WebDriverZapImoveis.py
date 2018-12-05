#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep

delay = 10
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("""--user-agent=Mozilla/5.0 
                            (X11; Linux x86_64) 
                            AppleWebKit/537.36 
                            (KHTML, like Gecko) 
                            Chrome/47.0.2526.80 
                            Safari/537.36""")

driver = webdriver.Chrome(chrome_options=chrome_options)
print("Starting Chrome Headless...")

driver.get('https://www.zapimoveis.com.br/')

btn_rent = WebDriverWait(driver,delay).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='btnLocacao']")
            )
        )
btn_rent.click()

opt_selector = WebDriverWait(driver,delay).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='tipoImovelNovo']/optgroup[1]/option")
            )
        )
opt_selector.click()

btn_search = WebDriverWait(driver,delay).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='btnBuscar']")
            )
        )
btn_search.click()

soup = BeautifulSoup(driver.page_source, "html.parser")

article_list = driver.find_element_by_id("list")

#article_list = WebDriverWait(driver,delay).until(
#        EC.visibility_of_element_located(
#            (By.XPATH, "//*[@id='list']")
#            )
#        )

print(article_list.text)

'''
article_list = soup.find("div", {"id" : "list"})
article = article_list.findChildren("article", recursive=False)

for child in article:
    print(child)
'''





