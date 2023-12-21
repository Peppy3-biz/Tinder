import pyautogui
import pygetwindow as gw
from pywinauto.application import Application
from time import sleep

for window in gw.getAllTitles():
    if "Tinder | Dating," in window:
        window_name = window

def click(image):
    thingLocation = pyautogui.locateOnScreen(image)
    if thingLocation:
        pyautogui.click(thingLocation)
    else:
        return 'not found'

# Name of the window you want to focus
#window_name = "Tinder | Dating, Make Friends & Meet New People and 7 more pages - Personal - Microsoft​ Edge"

# Find the window
#try: 
window = gw.getWindowsWithTitle(window_name)[0]
'''except:
    window_name = 
print(window)'''

# Focus the window
if window is not None:
    app = Application().connect(handle=window._hWnd)
    app_window = app.window(handle=window._hWnd)
    app_window.set_focus()


networkImage = r"C:\Users\Unhap\OneDrive\Documents\GitHub\Tinder\TinderBot\TextingFunctionality\networkTab.png"
if click(networkImage) == 'not found':
    pyautogui.hotkey('ctrl', 'shift', 'i')
    sleep(1)
    if click(networkImage):
        print("Error: Can't find Network Tab")

# Refresh the page to get Network Data
pyautogui.press('f5')

