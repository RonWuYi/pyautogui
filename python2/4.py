import pyautogui
pyautogui.PAUSE = 1

try:
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
except:
    print "except"

# while True:
pyautogui.PAUSE = 1
pyautogui.moveTo(600, 600)
pyautogui.PAUSE = 1
# pyautogui.click()
# pyautogui.PAUSE = 1

# pyautogui.PAUSE = 1
# pyautogui.moveTo(812, 455)
# pyautogui.PAUSE = 1
# pyautogui.click()
# pyautogui.PAUSE = 1

# pyautogui.PAUSE = 0.9
# screenW, screenH = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
# print currentMouseY, currentMouseY