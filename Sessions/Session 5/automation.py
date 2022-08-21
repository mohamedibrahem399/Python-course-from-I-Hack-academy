import pyautogui
import time

print(pyautogui.size())

program = """

import random

import random


def get_input():
	num = int(input("please enter your guess: "))
	return num


random_number = random.randint(0,100)

chances = 3


print("guess a number between 0 and 100: ")


guess = get_input()

while guess != random_number and chances >=0:
	if guess > random_number:
		print('you guessed higher \n')
		chances -= 1
		guess = get_input()
	elif guess < random_number:
		print("you guessed lower \n")
		chances -= 1
		guess = get_input()
if guess == random_number:
	print("you won!!")
elif guess != random_number:
	print("you lost!")
"""

#21, 740 starprintt menu location
#write s
# 165, 177 sublime text location
# while True:
# 	print(pyautogui.position())
pyautogui.moveTo(21,740, duration=10)
pyautogui.click(21,740)
time.sleep(1)
pyautogui.typewrite('s')
time.sleep(1)
pyautogui.moveTo(165,177,duration=1)
pyautogui.click(165,177)
pyautogui.press('start')
pyautogui.click(1167,244)
pyautogui.typewrite(program,interval=0.1)
pyautogui.hotkey('ctrl','s')