import pyautogui
import subprocess
import time
import autoit
import datetime
import pyperclip
import win32com.client as win32
import os
from tkinter import Tk
from ctypes import *
windll.user32.BlockInput(True)  # enable block
windll.user32.BlockInput(True)  # enable block

while not pyautogui.locateOnScreen("Png/ENG.png"):
    time.sleep(0.1)
    pyautogui.hotkey("Ctrl", "Shift")
os.system('TASKKILL /F /IM Technologist.exe')
path = "D:/NEW TECHnologist/"
autoit.run(path + "Technologist.exe")
autoit.win_wait_active("TECHNOLOGIST LOAD", 9999)
time.sleep(2)
while True:
    if pyautogui.locateOnScreen("Png/Znach.png"):
        break
    time.sleep(0.1)
time.sleep(1)
pyautogui.doubleClick(pyautogui.locateCenterOnScreen('Png/Znach.png'))
while True:
    if pyautogui.locateOnScreen("Png/Ageyev.png"):
        break
    time.sleep(0.1)
time.sleep(1)
pyautogui.doubleClick(pyautogui.locateCenterOnScreen('Png/Ageyev.png'))
pyautogui.doubleClick(pyautogui.locateCenterOnScreen('Png/Ageyev.png'))
while True:
    if pyautogui.locateOnScreen("Png/button1.png"):
        break
    time.sleep(0.1)
time.sleep(1)
pyautogui.doubleClick(pyautogui.locateCenterOnScreen('Png/button1.png'))
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
time.sleep(2)
while True:
    if pyautogui.locateOnScreen("Png/plan.png"):
        break
    time.sleep(0.1)
time.sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen('Png/plan.png'))
time.sleep(0.5)
autoit.mouse_wheel("up", 20)

while True:
    if pyautogui.locateOnScreen("Png/minipech.png"):
        break
    time.sleep(0.1)
try: pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/minipech.png')))
except: time.sleep(0.1)

while True:
    time.sleep(1)
    if not pyautogui.locateOnScreen("Png/lupa2.png"):
        break

while True:
    if pyautogui.locateOnScreen("Png/zagruzka1.png"):
        break
    time.sleep(0.1)
try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/zagruzka1.png')))
except: time.sleep(0.1)

while True:
    if pyautogui.locateOnScreen("Png/zagruzka2.png"):
        break
    time.sleep(0.1)
try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/zagruzka2.png')))
except: time.sleep(0.1)

while True:
    if pyautogui.locateOnScreen("Png/msg1.png"):
        break
    time.sleep(0.2)

os.system('TASKKILL /F /IM Technologist.exe')
now = datetime.datetime.now()
year = str(now.year-2000)
day = str(now.day)
if len(day) == 1:
    day = "0"+day
month = str(now.month)
if len(month) == 1:
    month = "0"+month
hour = str(now.hour)
if len(hour) == 1:
    hour = "0"+hour
minute = str(now.minute)
if len(minute) == 1:
    minute = "0"+minute
file = "Report/Отчет "+year+"."+month+"."+day+".00.00-"+year+"."+month+"."+day+"."+hour+"."+minute+".xml"

while True:
    time.sleep(0.1)
    if os.path.isfile("D:/NEW TECHnologist/"+file):
        break
while True:
    if pyautogui.getWindowsWithTitle("Report"):
        autoit.win_close("Report")
        break
    time.sleep(0.1)

excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open("D:/NEW TECHnologist/"+file)
excel.Visible = False
excel.DisplayAlerts = False
wb.DoNotPromptForConvert = True
wb.CheckCompatibility = False
ws = wb.Worksheets('K5, Мини печи')
ws.Activate
i = 2
st = ""

while True:
    if str(ws.Range("G" + str(i))) == str(ws.Range("G" + str(i+1))):
        break
    st = st + os.linesep + str(ws.Range("G"+str(i)))
    i += 1
pyperclip.copy(st)

os.system('TASKKILL /F /IM Excel.exe')
os.system('TASKKILL /F /IM saplogon.exe')
time.sleep(1)
subprocess.Popen(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")

while True:
    if pyautogui.locateOnScreen("Png/SAP1.png"):
        break
    time.sleep(0.1)
try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP1.png')))
except: time.sleep(0.1)

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
if pyautogui.locateOnScreen("Png/SAP3.png"):
    try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP3.png')))
    except: time.sleep(0.1)
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
try: pyautogui.click('Png/SAP6.png')
except: time.sleep(0.1)
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
try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP8.png')))
except: time.sleep(0.1)
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
try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP9.png')))
except: time.sleep(0.1)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
bufer = Tk().clipboard_get()

os.system('TASKKILL /F /IM saplogon.exe')
time.sleep(1)
subprocess.Popen(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")

while True:
    if pyautogui.locateOnScreen("Png/SAP1.png"):
        break
    time.sleep(0.1)
try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP1.png')))
except: time.sleep(0.1)

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
    try: pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/SAP3.png')))
    except: time.sleep(0.1)
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
pyautogui.write("-----" + len(s) + " ta bo'ldi. -----")
pyautogui.press("enter")
