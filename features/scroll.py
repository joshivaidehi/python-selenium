from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://wikipedia.org')

elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(5)
elm.send_keys(Keys.HOME)