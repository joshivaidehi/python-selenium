#Assert page title in Python selenium webdriver.

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://google.com')

try:
    assert 'Google' in driver.title
    print('test pass')

except Exception as e:
    print('exception',format(e))