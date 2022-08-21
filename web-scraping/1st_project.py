import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib.request
from bs4 import BeautifulSoup
from xlsxwriter import Workbook

workbook=Workbook('tourism_info.xlsx')

driver = webdriver.Chrome()
driver.get("https://www.tripadvisor.com/Attractions-g294200-Activities-c26-Egypt.html")

main_urls=driver.find_elements_by_xpath("//a[@class='poiTitle ']")
main_url=[]

worksheet=workbook.add_worksheet()



for main_url in main_urls:
	main_url.click()
	try :
		#define objects in the hyper link
		maps=driver.find_elements_by_xpath("//img[@class='mapImg']")

		location= driver.find_elements_by_xpath("div[@class='address']")
		print (location)

		#city_element= driver.find_elements_by_xpath("span[@class='locality']")
		#country_element=driver.find_elements_by_xpath("span[@class='country-name']")
		#city=city_element.text
		#country=country_element.text
		#print (city,country)


		attraction_word = driver.find_elements_by_xpath("div[@class='attractions-attraction-detail-about-card-AttractionDetailAboutCard__section--1_Efg attractions-attraction-detail-about-card-AttractionDetailAboutCard__title--6-Ao-']")
		print (attraction_word)


		descriptions =driver.find_elements_by_xpath("def[@class='attractions-attraction-detail-about-card-AttractionDetailAboutCard__section--1_Efg']")
		print (descriptions)

		#data_array=[location_test , real_attraction_word , real_descriptions ]
		#for i in range (len(data_array)):
		#	worksheet.write(0,i,data_array[i])

	finally :
		driver.close()




