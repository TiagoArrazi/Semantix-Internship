#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from time import sleep

driver = webdriver.Chrome()
action = action_chains.ActionChains(driver)

driver.get("https://www.youtube.com/watch?v=8ZtInClXe1Q")

sleep(1)

driver.find_element_by_xpath("//ytd-toggle-button-renderer[@class='style-scope ytd-menu-renderer force-icon-button style-text']").click()
driver.find_element_by_xpath("//*[@class='style-scope ytd-modal-with-title-and-button-renderer style-blue-text size-default']").click()
driver.find_element_by_xpath("//input[@type='email']").send_keys("tiago.costa@semantix.com.br")
driver.find_element_by_id("identifierNext").click()

sleep(1)

driver.find_element_by_xpath("//input[@type='password']").send_keys("morrados2018!@#")
driver.find_element_by_id("passwordNext").click()

sleep(1)

driver.find_element_by_xpath("//ytd-toggle-button-renderer[@class='style-scope ytd-menu-renderer force-icon-button style-text']").click()
