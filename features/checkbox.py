from selenium import webdriver
from selenium.webdriver.common import keys 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://demos.dojotoolkit.org/dijit/tests/form/test_CheckBox.html')

driver.find_elements_by_xpath(".//*[contains(text(),'cb7: normal checkbox.')]").click()
