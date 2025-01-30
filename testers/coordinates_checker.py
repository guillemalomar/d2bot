import pyautogui
import time

current_iteration = 0
while current_iteration < 1000:
    time.sleep(5)
    print(pyautogui.position())
    current_iteration += 1