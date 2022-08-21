import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib.request
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=mBSHLPhbsLs")
time.sleep(2)
videos = driver.find_elements_by_class_name("html5-video-container")

while True:
    try :
        videos = driver.find_elements_by_tag_name("video")
        i=0
        for video in videos:
            if i<20 :
                i=i+1
                print(video.get_attribute('src'),"\n" )
                url= video.get_attribute('src')
                urllib.request.urlretrieve(url, '\\Users\\Mohamed ibrahem\\Downloads/pic'+str(i)+'.mp4')
                time.sleep(0.05)

    except:
        i=i+1
        continue
    finally:
        driver.close()
        break