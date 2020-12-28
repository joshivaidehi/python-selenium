from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://codepad.org')

text_area = driver.find_element_by_id('textarea')
text_area.send_keys("This text is send using Python code.")