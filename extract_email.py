#extract emails from the website 

from selenium import webdriver
import re

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("http://www.airindia.in/contact-details.htm")

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+',doc)

for email in emails:
    print(email)