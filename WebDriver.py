#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PW import getAP_631

delay = 10
identity = "automatontest631@gmail.com"
comment = "This comment was sent by an automation software made with Selenium and Python"
url = "https://www.youtube.com/watch?v=8ZtInClXe1Q&t=1s"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)

signInButton = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, "//ytd-button-renderer[@class='style-scope ytd-masthead style-blue-text size-default']")))
signInButton.click()

idTextField = WebDriverWait(driver,delay).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
idTextField.send_keys(identity)
idTextField.send_keys(keys.Keys.ENTER)

pwTextField = WebDriverWait(driver,delay).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
pwTextField.send_keys(getAP_631())
pwTextField.send_keys(keys.Keys.ENTER)

YTLikeButton = WebDriverWait(driver,delay).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]")))
YTLikeButton.click()

driver.execute_script("window.scrollTo(0, 450)") 

YTUnclickedCommentTextField = WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='placeholder-area']")))
YTUnclickedCommentTextField.click()

YTClickedCommentTextField = driver.find_element_by_xpath("//*[@id='contenteditable-textarea']")
YTClickedCommentTextField.send_keys(comment)

commentButton = WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit-button']")))
commentButton.click()
