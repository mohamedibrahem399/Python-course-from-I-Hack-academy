import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request


driver = webdriver.Chrome()
driver.get("https://www.tripadvisor.com/Attraction_Review-g294201-d308884-Reviews-Khan_Al_Khalili-Cairo_Cairo_Governorate.html")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)
map_pic= driver.find_elements_by_xpath("//img[@class='mapImg']")
print (map_pic)
time.sleep(2)

for maps in map_pic:

	print(maps.get_attribute('src'),"\n" )
	url = maps.get_attribute('src')
	i=0
	urllib.request.urlretrieve(url, '\\Users\\Mohamed ibrahem\\Downloads/pic'+str(i)+'.jpg')
time.sleep(0.05)

driver.close()