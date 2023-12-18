import pyautogui
import pygetwindow as gw
from pywinauto.application import Application
from time import sleep

# Name of the window you want to focus
window_name = "Tinder | Dating, Make Friends & Meet New People and 7 more pages - Personal - Microsoft​ Edge"

# Find the window
window = gw.getWindowsWithTitle(window_name)[0]

# Focus the window
if window is not None:
    app = Application().connect(handle=window._hWnd)
    app_window = app.window(handle=window._hWnd)
    app_window.set_focus()


networkImage = r"C:\Users\Unhap\OneDrive\QuickUse\TinderBot\TextingFunctionality\networkTab.png"
networkTabLocation = pyautogui.locateOnScreen(networkImage)
if networkTabLocation:
    pyautogui.click(networkTabLocation)
else:
    pyautogui.hotkey('ctrl', 'shift', 'i')
    sleep(1)
    if networkTabLocation:
        pyautogui.click(networkTabLocation)

# Refresh the page to get Network Data
pyautogui.press('f5')

