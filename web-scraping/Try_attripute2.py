import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=ings&rlz=1C1SSYD_enEG864EG864&source=lnms&tbm=isch&sa=X&ved=0ahUKEwitn9uVl9HlAhUDAmMBHU2iBuAQ_AUIEygC&biw=1600&bih=789#imgrc=_")

imges=driver.find_elements_by_xpath("//div[@class='THL2l']")
print (imges)
for imge in imges :
	print (imge.get_attribute("src"))

time.sleep(1)

driver.close()
