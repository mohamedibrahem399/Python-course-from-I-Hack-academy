from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome ()
driver.get("http://quotes.toscrape.com/")	

quotes = driver.find_elements_by_xpath("//span[@class='text']")
authors = driver.find_elements_by_xpath("//small[@class='author']")





while True :

	quotes = driver.find_elements_by_xpath("//span[@class='text']")
	authors = driver.find_elements_by_xpath("//small[@class='author']")
	with open ('sss.txt','a') as file:
		for i in range (len(quotes)):
			print(i)
			file.write(quotes[i].text + '\n' + authors[i].text + '\n')
		file.close()
	time.sleep(1)
	next_button = driver.find_element_by_xpath("//li[@class='next']//a")
	next_button.click()

