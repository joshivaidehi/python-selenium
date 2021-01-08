from selenium import webdriver
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
import csv
import pandas

query_keyword = "Devops"
no_of_pages = 1
email = "your email"
password = "your password"

driver = webdriver.Chrome(executable_path='/home/devx/selenium/Linkedin-Scraper/chromedriver')
driver.get('https://www.linkedin.com/login')

email_box = driver.find_element_by_id('username')
email_box.send_keys(email)
pass_box = driver.find_element_by_id('password')
pass_box.send_keys(password)
submit_button = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
submit_button.click()

time.sleep(1)

urls = []
for i in tqdm(range(no_of_pages)):
	try:
		driver.get(
			'https://www.linkedin.com/search/results/people/?'
			'origin=FACETED_SEARCH&page=' + str(i) +
			'&title=' + query_keyword
		)
		soup = BeautifulSoup(driver.page_source, "lxml")
		soup = soup.find_all(class_="search-result__result-link")
		for s in soup:
			url = 'https://www.linkedin.com' + s['href']
			urls.append(url)
		print(i)
	except KeyboardInterrupt:
		break

urls = list(set(urls))
print("n".join(urls))

print(urls)
with open(query_keyword + "Urls.txt", "w") as f:
	urls = f.write(urls)

# with open('protagonist.csv', 'wb') as f:
#  	for url in urls:
#  		writer = csv.writer(f)
#  		writer.writerow(url)

# myFile = open('csvexample3.csv', 'a')
# with myFile:
#    writer = csv.writer(myFile)
#    writer.writerows(urls)


