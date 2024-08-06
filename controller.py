import pyautogui
import time
import pyperclip


path = 'C:/Users/Baranyai Ferenc/Desktop/Git/ChessAI/ChessAI/'
dir = 'source/locations/'

def findAndClick(img):
    location = pyautogui.locateOnScreen(path+dir+img, confidence=0.8)

    if location is not None:
        pyautogui.click(pyautogui.center(location))

def CopyFEN():
    time.sleep(5)
    findAndClick('share.png')
    time.sleep(1)
    findAndClick('png.png')
    time.sleep(1)
    pyautogui.press('tab')

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(1)
    
    findAndClick('close.png')

    return pyperclip.paste()
