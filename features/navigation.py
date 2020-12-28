from selenium import webdriver
from selenium.webdriver.common import keys
import time 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://google.com')

elem = driver.find_element_by_link_text('About')
time.sleep(2)
elem.click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
