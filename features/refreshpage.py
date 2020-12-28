import time 
from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://wikipedia.org')

time.sleep(3)
driver.refresh()
time.sleep(2)
driver.close()