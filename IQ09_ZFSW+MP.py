import pyautogui
import subprocess
import time
import autoit
import os
from tkinter import Tk
from ctypes import *
windll.user32.BlockInput(True)  # enable block

os.system('TASKKILL /F /IM saplogon.exe')

time.sleep(1)
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
pyautogui.write("shusanov")
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.write("535650500")
pyautogui.press("enter")

i = 1
while True:
    if pyautogui.locateOnScreen("Png/SAP3.png"):
        break
    time.sleep(0.1)
    if i == 30:
        break
    i += 1
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP3.png')))
time.sleep(0.1)
pyautogui.press("enter")

while True:
    if pyautogui.locateOnScreen("Png/SAP4.png"):
        break
    time.sleep(0.1)
pyautogui.press("F3")

time.sleep(1)

while True:
    if pyautogui.locateOnScreen("Png/SAP5.png"):
        break
    time.sleep(0.1)
pyautogui.write("IQ09")
pyautogui.press("enter")

while True:
    if pyautogui.locateOnScreen("Png/SAP6.png"):
        break
    time.sleep(0.1)
pyautogui.click('Png/SAP6.png')
time.sleep(1)

pyautogui.hotkey("shift", "F4")
time.sleep(0.5)
pyautogui.hotkey("shift", "F12")
time.sleep(2)
pyautogui.press("F8")
time.sleep(1)
pyautogui.press("F8")

while True:
    if pyautogui.locateOnScreen("Png/SAP8.png"):
        break
    time.sleep(0.1)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP8.png')))
time.sleep(0.1)
pyautogui.hotkey("Ctrl", "Shift", "F2")
time.sleep(0.5)
pyautogui.press("space")
pyautogui.press("down")
pyautogui.press("enter")
time.sleep(0.1)
pyautogui.press("enter")
time.sleep(1)

for a in range(20):
    autoit.send("{pgdn}")
    time.sleep(0.1)

pyautogui.hotkey("ctrl", "end")
time.sleep(0.5)

while True:
    if pyautogui.locateOnScreen("Png/SAP9.png"):
        break
    time.sleep(0.1)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP9.png')))
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
bufer = Tk().clipboard_get()

os.system('TASKKILL /F /IM saplogon.exe')
time.sleep(1)
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
time.sleep(1)

s = str.split(bufer, "\n")
for i in range(len(s)):
    pyautogui.write(s[i])
    pyautogui.press("enter")
    time.sleep(1)
