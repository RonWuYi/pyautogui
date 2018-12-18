import pyautogui
import time

pyautogui.PAUSE = 1

def TabQieHuan():
    try:
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    except:
        print "except"

def JinYanGongXun():
    pyautogui.moveTo(1508, 345)
    pyautogui.click()

    # clict "shua xin"
    pyautogui.moveTo(910, 570)
    pyautogui.click()
    time.sleep(9)

    # clict "jie shou ren wu"/" qu wan cheng ren wu"
    pyautogui.moveTo(800, 612)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(109)

    pyautogui.moveTo(1480, 345)
    pyautogui.click()

    # click "san bei jiang li"
    pyautogui.moveTo(900, 555)
    pyautogui.click()

    for i in range(9):
        # clict "shua xin"
        pyautogui.moveTo(910, 570)
        pyautogui.click()
        time.sleep(9)

        # clict "jie shou ren wu"/" qu wan cheng ren wu"
        pyautogui.moveTo(800, 612)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
        time.sleep(120)

        pyautogui.moveTo(1480, 345)
        pyautogui.click()

        # click "san bei jiang li"
        pyautogui.moveTo(900, 555)
        pyautogui.click()

def YingXiongTianFu():
    # chuan
    pyautogui.moveTo(1519, 345)
    pyautogui.click()

    # clict "jie shou ren wu"/" qu wan cheng ren wu"
    pyautogui.moveTo(800, 612)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(240)

    # chuan
    pyautogui.moveTo(1474, 345)
    pyautogui.click()

    # click "san bei jiang li"
    pyautogui.moveTo(900, 555)
    pyautogui.click()

    for j in range(9):
        # clict "jie shou ren wu"/" qu wan cheng ren wu"
        pyautogui.moveTo(800, 612)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
        time.sleep(240)
        # pyautogui.PAUSE = 240

        # chuan
        pyautogui.moveTo(1474, 345)
        pyautogui.click()

        # click "san bei jiang li"
        pyautogui.moveTo(900, 555)
        pyautogui.click()

# Todo
def WeiWangRenWu():
    pass

def TaFangFuBen():
    for jj in range(4):
        # pyautogui.moveTo(1505, 422)
        pyautogui.moveTo(1519, 349)
        pyautogui.click()

        # jin ru feng mo gu
        pyautogui.moveTo(790, 635)
        pyautogui.click()

        # kai shi shua guai
        pyautogui.moveTo(990, 545)
        pyautogui.click()

        for ii in range(2):
            # dian
            pyautogui.moveTo(610, 545)
            pyautogui.click()

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.click(button='right', clicks=1)

            # du
            pyautogui.moveTo(700, 545)
            pyautogui.click()

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.click(button='right', clicks=1)

            # bin
            pyautogui.moveTo(800, 545)
            pyautogui.click()

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.click(button='right', clicks=1)

            # bao
            pyautogui.moveTo(890, 545)
            pyautogui.click()

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.click(button='right', clicks=1)

            # deng dai jie shu
            time.sleep(500)

            # lin qu jiang li
            pyautogui.moveTo(900, 425)
            pyautogui.click()
            # # dao lu dian ji dian
            # pyautogui.moveTo(1300, 410)

def CaiLiaoFuBen():
    moveValue = 30;
    for iii in range(0, 10):

        # chuan
        pyautogui.moveTo(1512, 385)
        pyautogui.click()

        # fu ben ming zi
        pyautogui.moveTo(801, (445 + (iii * moveValue)))
        # xia yi 10 pixels
        pyautogui.click()

        # jin ru fu ben
        pyautogui.moveTo(789, 629)
        pyautogui.click()

        # zi dong zhan dou
        pyautogui.press('z')
        time.sleep(200)

        # tui chu fu ben
        pyautogui.moveTo(1435, 530)
        pyautogui.click()

def HuiShouWuPin():
    pyautogui.moveTo(1460, 540)
    pyautogui.click()
    pyautogui.moveTo(810, 456)
    pyautogui.click()
    pyautogui.moveTo(889, 602)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(1092, 601)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)

# Todo
def GuaJi():
    # move click gua ji
    pyautogui.moveTo(1492, 575)
    pyautogui.click()
    pyautogui.moveTo(692, 465)
    pyautogui.click()
    pyautogui.press('m')
    pyautogui.moveTo(494, 367)
    pyautogui.click()

# Todo
def WaKuang():
    pyautogui.moveTo(1220, 611)
    time.sleep(100)
    pyautogui.click()



