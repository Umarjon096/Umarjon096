import pyautogui
import time
while not pyautogui.locateOnScreen("Png/ENG.png"):
    time.sleep(0.1)
    pyautogui.hotkey("Ctrl", "Shift")
