import pyautogui
def open_folder():
	cords2=pyautogui.locateCenterOnScreen("new_folder_photo.png")
	pyautogui.doubleClick(cords2)
	print(cords2)

open_folder()