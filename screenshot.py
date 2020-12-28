
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('https://devx.work/collab')
driver.save_screenshot("screenshot.png")

driver.close()