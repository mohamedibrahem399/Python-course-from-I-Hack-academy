import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

driver = webdriver.Chrome()
driver.get("")

imges=driver.find_elements_by_xpath("//img[@class='alignnone']")
print (imges)
for imge in imges :
	print (imge.get_attribute("src"))

time.sleep(1)

driver.close()
