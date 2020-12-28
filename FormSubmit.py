#input and button type to submit form.

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://codepad.org')

python_button = driver.find_element_by_xpath("/html/body/div[1]/center/table/tbody/tr/td[1]/div/form/table/tbody/tr[2]/td[1]/nobr[10]/label/input")
python_button.click()

text_area = driver.find_element_by_id('textarea')
text_area.send_keys("This text is send using Python code.")

button = driver.find_element_by_xpath("/html/body/div[1]/center/table/tbody/tr/td[1]/div/form/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/button")
button.click()

