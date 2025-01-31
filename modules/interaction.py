import random
import time

import pyautogui

pyautogui.FAILSAFE = False

def click(x=None, y=None, button="left", time_low=1, time_high=1.5):
    time.sleep(random.uniform(time_low, time_high))
    if x:
        pyautogui.click(x=random.uniform(x-2, x+2), y=random.uniform(y-2, y+2), button=button)
    else:
        pyautogui.click(button=button)

def keyboard_press(key_to_press, time_low=0.5, time_high=1):
    time.sleep(random.uniform(time_low, time_high))
    pyautogui.press(key_to_press)

def control_click(x, y, button="left", time_low=0.5, time_high=1):
    time.sleep(random.uniform(time_low, time_high))
    pyautogui.keyDown('ctrl')
    pyautogui.click(x=random.uniform(x-3, x+3), y=random.uniform(y-3, y+3), button=button)
    pyautogui.keyUp('ctrl')

def move_mouse(x, y):
    pyautogui.moveTo(x, y)

def check_if_started():
    current_try = 0
    while current_try < 30:
        time.sleep(2)
        if pyautogui.pixel(100, 100) != (0, 0, 0):
            return
        current_try += 1
    exit(500)
