import pyautogui
import time
import autoit
import os
from ctypes import *
windll.user32.BlockInput(True)  # enable block

os.system('TASKKILL /F /IM Technologist.exe')
path = "D:/NEW TECHnologist/"
autoit.run(path+"Technologist.exe")
autoit.win_wait_active("TECHNOLOGIST LOAD", 9999)
time.sleep(0.1)
while True:
    if pyautogui.locateOnScreen("Png/Znach.png"):
        break
    time.sleep(0.1)
try:
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/Znach.png')))
except:
    time.sleep(0.1)
while True:
    if pyautogui.locateOnScreen("Png/Ageyev.png"):
        break
    time.sleep(0.1)
try:
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/Ageyev.png')))
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/Ageyev.png')))
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/Ageyev.png')))
except:
    time.sleep(0.1)

while True:
    if pyautogui.locateOnScreen("Png/button1.png"):
        break
    time.sleep(0.1)
try:
    pyautogui.doubleClick('Png/button1.png')
    pyautogui.doubleClick('Png/button1.png')
except:
    time.sleep(0.1)
time.sleep(1)
autoit.send("{NUMPAD9 2}")
autoit.send("{NUMPAD8}")
autoit.send("{NUMPAD5}")
autoit.send("{NUMPAD0}")
autoit.send("{NUMPAD9}")
autoit.send("{NUMPAD5}")
time.sleep(0.5)
autoit.send("{Enter}")
autoit.win_wait_active("TECHNOLOGIST", 9999)
