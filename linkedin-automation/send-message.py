import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
import time 

import chromedriver_binary
from selenium import webdriver
browser = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')

browser.get('https://www.linkedin.com/login')

elementID = browser.find_element_by_id('username')
elementID.send_keys('Enter username')
elementID = browser.find_element_by_id('password')
elementID.send_keys('enter password')
elementID.submit()

fullLink = 'https://www.linkedin.com/in/dharmik-boricha-816075170/'
browser.get(fullLink)

browser.find_element_by_class_name("pv-s-profile-actions").click()
time.sleep(3)

browser.find_element_by_class_name("message-anywhere-button pv-s-profile-actions pv-s-profile-actions--message ml2 artdeco-button artdeco-button--2 artdeco-button--primary").click()
time.sleep(3)

browser.find_element_by_css_selector('.msg-form__contenteditable').send_keys("Hi, hope you are keeping well, it would be good to connect.")
time.sleep(3)




