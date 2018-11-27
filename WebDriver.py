#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=8ZtInClXe1Q")
driver.find_element_by_xpath("//ytd-toggle-button-renderer[@class='style-scope ytd-menu-renderer force-icon-button style-text']").click()
driver.find_element_by_xpath("//*[@class='style-scope ytd-modal-with-title-and-button-renderer style-blue-text size-default']").click()
driver.find_element_by_xpath("//input[@type='email']").send_keys("tiago.costa@semantix.com.br")
driver.find_element_by_id("identifierNext").click()
driver.find_element_by_xpath("//*[@type='password']").send_keys("123")
