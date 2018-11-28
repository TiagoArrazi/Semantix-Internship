#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from time import sleep

driver = webdriver.Chrome()
action = action_chains.ActionChains(driver)
driver.maximize_window()

driver.get("https://www.youtube.com/watch?v=8ZtInClXe1Q&t=1s")

sleep(2)

driver.find_element_by_xpath("//ytd-button-renderer[@class='style-scope ytd-masthead style-blue-text size-default']").click()#Sign in button

driver.find_element_by_xpath("//input[@type='email']").send_keys("tiago.costa@semantix.com.br")
driver.find_element_by_id("identifierNext").click()

sleep(1)

driver.find_element_by_xpath("//input[@type='password']").send_keys("morrados2018!@#")
driver.find_element_by_id("passwordNext").click()

sleep(5)

driver.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]").click()
driver.execute_script("window.scrollTo(0, 450)") 

sleep(3)

driver.find_element_by_xpath("//*[@id='placeholder-area']").click()
driver.find_element_by_xpath("//*[@id='contenteditable-textarea']").send_keys("This comment was sent by an automation software made with Selenium and Python")

sleep(3)

driver.find_element_by_xpath("//*[@id='submit-button']").click()
