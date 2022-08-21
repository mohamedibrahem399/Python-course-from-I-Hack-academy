from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome ()
driver.get("https://www.google.com/?hl=ar")	

elem=driver.find_element_by_name("q")
elem.clear()
elem.send_keys("python")
time.sleep(1)
elem.send_keys(Keys.RETURN)

