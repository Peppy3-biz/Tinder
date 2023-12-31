import pyautogui
import pygetwindow as gw
from pywinauto.application import Application
from time import sleep

# Find the window
for window in gw.getAllTitles():
    if "Tinder | Dating," in window:
        window_name = window
if not window_name:
    print("Tinder not found")

# Open the window 
window = gw.getWindowsWithTitle(window_name)[0]

# Focus the window
if window is not None:
    app = Application().connect(handle=window._hWnd)
    app_window = app.window(handle=window._hWnd)
    app_window.set_focus()



def click(image, confidenceLevel):
    thingLocation = pyautogui.locateOnScreen(image, confidence=confidenceLevel)
    if thingLocation:
        pyautogui.click(thingLocation)
    else:
        return 'not found'





networkImage = r"C:\Users\Unhap\OneDrive\Documents\GitHub\Tinder\TinderBot\TextingFunctionality\imageReferences\networkTab.png"
messagesImage = r"C:\Users\Unhap\OneDrive\Documents\GitHub\Tinder\TinderBot\TextingFunctionality\imageReferences\lightenedMessagesJSON.png"
if click(networkImage, .9) == 'not found':
    pyautogui.hotkey('ctrl', 'shift', 'i')
    sleep(1)
    if click(networkImage, .9):
        print("Error: Can't find Network Tab")

# Refresh the page to get Network Data
pyautogui.press('f5')

