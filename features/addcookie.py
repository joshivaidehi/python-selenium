from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('https://bing.com')

cookie = {'fruit':'mango','chocolate':'milk'}
driver.add_cookie(cookie)

print(driver.get_cookies())