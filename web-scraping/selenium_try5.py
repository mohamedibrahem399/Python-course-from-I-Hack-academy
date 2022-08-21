import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib.request
driver = webdriver.Chrome()
driver.get("https://unsplash.com/images")
while True:
    try :
        images = driver.find_elements_by_tag_name('img')
        i=0
        for image in images:
            if i<10 :
            	i=i+1
            	print(image.get_attribute('src'),"\n" )
            	url = image.get_attribute('src')
            	urllib.request.urlretrieve(url, '\\Users\\Mohamed ibrahem\\Downloads/pic'+str(i)+'.jpg')
            	time.sleep(0.05)
    finally:
        driver.close()
        break