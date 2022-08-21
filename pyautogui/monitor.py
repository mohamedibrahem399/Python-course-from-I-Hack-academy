import pyautogui as p
import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
print (pyautogui.position())
#for i in range (50, 1000, 50):
#	pyautogui.moveTo(i,i)
pyautogui.moveTo(487,684)
time.sleep(5)
pyautogui.doubleClick(487,684)
#time.sleep(5)
#pyautogui.moveTo(1309,75)
#pyautogui.click()
