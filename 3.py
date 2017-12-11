import pyautogui
pyautogui.PAUSE = 1

try:
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
except:
    print "except"
pyautogui.PAUSE = 1
#################################################
# ta fang jing yan
#################################################
for jj in range(4):
    # pyautogui.moveTo(1505, 422)
    pyautogui.moveTo(1505, 385)
    pyautogui.PAUSE = 2
    pyautogui.click()
    pyautogui.PAUSE = 2

    # jin ru feng mo gu
    pyautogui.moveTo(790, 635)
    pyautogui.PAUSE = 2
    pyautogui.click()
    pyautogui.PAUSE = 2

    # kai shi shua guai
    pyautogui.moveTo(990, 545)
    pyautogui.PAUSE = 2
    pyautogui.click()
    pyautogui.PAUSE = 2

    for ii in range(2):
        # dian
        pyautogui.moveTo(610, 545)
        pyautogui.PAUSE = 2
        pyautogui.click()
        pyautogui.PAUSE = 2

        # dao lu dian ji dian, ren wu qian jin
        pyautogui.moveTo(1300, 410)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3


        # du
        pyautogui.moveTo(700, 545)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        # dao lu dian ji dian, ren wu qian jin
        pyautogui.moveTo(1300, 410)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3

        # bin
        pyautogui.moveTo(800, 545)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        # dao lu dian ji dian, ren wu qian jin
        pyautogui.moveTo(1300, 410)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3

        # bao
        pyautogui.moveTo(890, 545)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        # dao lu dian ji dian, ren wu qian jin
        pyautogui.moveTo(1300, 410)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        pyautogui.PAUSE = 3
        # # kaishi shua guai dian

    # deng dai jie shu
    pyautogui.PAUSE = 500
    # pyautogui.moveTo(990, 545)

    # lin qu jiang li
    pyautogui.moveTo(900, 425)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1