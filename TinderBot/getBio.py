import pyautogui
import pygetwindow as gw
from pywinauto.application import Application
from time import sleep
import pyperclip
from sys import exit

window_name = ''
# Find the window
for window in gw.getAllTitles():
    if "Tinder | Dating," in window:
        window_name = window

if window_name == '':
    print("Tinder not found")
    exit()

# Open the window 
window = gw.getWindowsWithTitle(window_name)[0]

# Focus the window
if window is not None:
    app = Application().connect(handle=window._hWnd)
    app_window = app.window(handle=window._hWnd)
    app_window.set_focus()


# Click something function
def click(image, confidenceLevel):
    thingLocation = pyautogui.locateOnScreen(image, confidence=confidenceLevel)
    if thingLocation:
        pyautogui.click(thingLocation)
    else:
        return 'not found'



# Exit DevTools if open
if click(r"C:\Users\Unhap\OneDrive\Documents\GitHub\Tinder\TinderBot\TextingFunctionality\imageReferences\exitDevTools.png", .99) == 'not found':
    devToolsStatus = 'closed'
    sleep(1.7)
else:
    devToolsStatus = 'open'

# Move mouse to bio
pyautogui.moveTo(1460, 760)
# Scroll to top
pyautogui.scroll(2000)
sleep(1.1)
# Click and hold
pyautogui.mouseDown(button='left')
pyautogui.moveTo(1895, 1010)
sleep(1)
pyautogui.mouseUp(button='left')
pyautogui.hotkey('ctrl', 'c')
bio = pyperclip.paste()
sleep(1)
print(bio)
