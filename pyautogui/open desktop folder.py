import pyautogui
def open_folder():
	cords2=pyautogui.locateCenterOnScreen("111.png")
	pyautogui.doubleClick(cords2)
	print(cords2)

open_folder()