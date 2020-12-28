from selenium import webdriver 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("https://devx.work")

#find all the ids of the page 

count = 0

ids = driver.find_elements_by_xpath('//*[@href]')

for ii in ids:
    count +=1
    print(ii.get_attribute('href'))

print(count)
#driver.close()