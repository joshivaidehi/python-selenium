#Program to view all links of devx.work and view count of links.

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('https://devx.work/collab')

count = 0

for a in driver.find_elements_by_xpath('.//a'):
    count +=1
    print(a.get_attribute('href'))

print(count)

driver.close()


# count = 0

# for a in driver.find_elements_by_xpath('.//a'):
#     if count <= 10:
#         link = a.get_attribute('href')
#         # driver.get(link)
#         print(link)
#         count +=1
    
#     # print(a.get_attribute('href'))

# print(count)