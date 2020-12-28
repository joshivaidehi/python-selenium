from selenium import webdriver 
from selenium.webdriver.common import keys


driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("https://google.com")

elm = driver.find_element_by_link_text('About')
driver.implicitly_wait(5)
elm.click()