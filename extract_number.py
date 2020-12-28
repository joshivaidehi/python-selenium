#extract number from the website 

from selenium import webdriver
import re

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("https://www.amtrak.com/contact-us/helpful-links-and-phone-numbers.html")

doc = driver.page_source

phones = re.findall(r'[\d]{3}-[\d]{3}-[\d]{4}',doc)

for phone in phones:
    print(phone)