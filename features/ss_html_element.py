from selenium import webdriver
from PIL import Image

# take screenshot
driver = webdriver.Chrome(executable_path='/home/devx/selenium/chromedriver')
driver.get('https://www.google.com');

element = driver.find_element_by_id("hplogo");
location = element.location;
size = element.size;
driver.save_screenshot("pageImage.png");

# crop image
x = location['x'];
y = location['y'];
width = location['x']+size['width'];
height = location['y']+size['height'];
im = Image.open('pageImage.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('element.png')

driver.quit()