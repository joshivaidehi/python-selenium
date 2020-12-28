from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("http://google.com")

try:
    driver.find_element_by_link_text('About')
    print('Test Pass:found link text')

except Exception as e:
    print('Exception occured', format(e))

driver.close