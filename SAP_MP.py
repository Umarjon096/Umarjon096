import pyautogui
import subprocess
import time
import os
from ctypes import *
windll.user32.BlockInput(True)  # enable block

# os.system('TASKKILL /F /IM saplogon.exe')
# time.sleep(1)
path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
subprocess.Popen(path)

while True:
    if pyautogui.locateOnScreen("Png/SAP1.png"):
        break
    time.sleep(0.1)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP1.png')))

while True:
    if pyautogui.locateOnScreen("Png/SAP2.png"):
        break
    time.sleep(0.1)
pyautogui.write("sborka-mp")
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.write("1232123")
pyautogui.press("enter")

i = 1
while True:
    if pyautogui.locateOnScreen("Png/SAP3.png"):
        break
    time.sleep(0.1)
    if i == 30:
        break
    i += 1
if pyautogui.locateOnScreen("Png/SAP3.png"):
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP3.png')))
    time.sleep(0.1)
    pyautogui.press("enter")

while True:
    if pyautogui.locateOnScreen("Png/SAP5.png"):
        break
    time.sleep(0.1)
pyautogui.write("ZFSW")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("1030")
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("F8")
