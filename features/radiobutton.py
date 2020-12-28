from selenium import webdriver
import time
from selenium.webdriver.common import keys 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('https://www.zkoss.org/zkdemo/input/radio_button')

for i in driver.find_elements_by_xpath("//*[@type='radio']"):
    i.click()

time.sleep(6)