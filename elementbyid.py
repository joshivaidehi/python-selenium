from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("http://www.google.com")

try:
    driver.find_element_by_tag_name('form')
    print('Test Pass: ID found')

except Exception as e:
    print("Exception found",format(e))

driver.close()