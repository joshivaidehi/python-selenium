import time 
from selenium import webdriver 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("https://google.com")

driver.quit()


