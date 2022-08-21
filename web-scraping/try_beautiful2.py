import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib.request 
from bs4 import BeautifulSoup

global str

driver = webdriver.Chrome()
driver.get("https://unsplash.com/images")
images = driver.find_elements_by_tag_name('img')


x=str(driver.page_source)


soup = BeautifulSoup(x,'html.parser')

print(soup.title.name)

driver.close()