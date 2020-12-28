from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('http://google.com')

count = 0

id = driver.find_elements_by_xpath('//*[@class]')

for all in id:
    count +=1
    print(all.get_attribute('class'))

print(count)

driver.close()