from selenium import webdriver 

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get("https://devx.work")

#find all the ids of the page 
ids = driver.find_elements_by_id('//*[@id]')

for ii in ids:
    print(ii.get_attribute('id'))

driver.close