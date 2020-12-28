from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('https://google.com')

body = driver.find_elements_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get('https://bing.com')
time.sleep(3)

driver.find_elements_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)
time.sleep(3)

driver.find_elements_by_tag_name(body).send_keys(Keys.CONTROL + 'w')
