import pyautogui
import keyboard
import random

num = [0,1]

while True:

    ram = random.choice(num)

    if ram == 0:
            pyautogui.click(x=1448, y=800, button="left")
            pyautogui.click(x=386, y=800, button="left")
            pyautogui.click(x=1824, y=900, button="left")
            pyautogui.click(x=857, y=600, button="left")
            pyautogui.click(x=1112, y=600, button="left")
    else:
            pyautogui.click(x=1448, y=800, button="left")
            pyautogui.click(x=386, y=800, button="left")
            pyautogui.click(x=1824, y=900, button="left")
            pyautogui.click(x=1112, y=600, button="left")
            pyautogui.click(x=857, y=600, button="left")
    if keyboard.is_pressed("s"):
        break