import pyautogui
import time
import datetime
import pyperclip
import win32com.client as win32
import autoit
import os
from ctypes import *
import os
from tkinter import Tk

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

while True:
    if pyautogui.locateOnScreen("Png/plan.png"):
        break
    time.sleep(0.1)
try:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/plan.png')))
except:
    time.sleep(0.1)
time.sleep(0.5)
autoit.mouse_wheel("up", 20)

while True:
    if pyautogui.locateOnScreen("Png/plity.png"):
        break
    time.sleep(0.1)
try:
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/plity.png')))
except:
    time.sleep(0.1)
while True:
    if pyautogui.locateOnScreen("Png/Filtr.png"):
        break
    time.sleep(0.1)
try:
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/Filtr.png')))
except:
    time.sleep(0.1)
while True:
    if pyautogui.locateOnScreen("Png/Pack.png"):
        break
    time.sleep(0.1)
try:
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('Png/Pack.png')))
except:
    time.sleep(0.1)


while True:
    if pyautogui.locateOnScreen("Png/lupa.png"):
        break
    time.sleep(0.1)
try:
    time.sleep(1)
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Png/lupa.png')))
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
ws = wb.Worksheets('K3, Кухонные плиты')
ws.Activate
i = 2
st = ""
while True:
    i += 1
    if str(ws.Range("G" + str(i))) == str(ws.Range("G" + str(i+1))):
        break
    st = st + os.linesep + str(ws.Range("G"+str(i)))
pyperclip.copy(st)

os.system('TASKKILL /F /IM Excel.exe')

