import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib.request
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=pictures&rlz=1C1SSYD_enEG864EG864&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiX2f7t5r3lAhVMKBoKHXVeAU4Q_AUIEigB&biw=987&bih=752#imgrc=doRL6HXjE6xaIM:")

while True:
    try :
        images = driver.find_elements_by_tag_name("img")
        i=0
        for image in images:
            if i<20 :
            	i=i+1
            	print(image.get_attribute('src'),"\n" )
            	url = image.get_attribute('src')
            	urllib.request.urlretrieve(url, '\\Users\\Mohamed ibrahem\\Downloads/pic'+str(i)+'.jpg')
            	time.sleep(0.05)
    except:
        i=i+1
        continue
    finally:
        driver.close()
        break

