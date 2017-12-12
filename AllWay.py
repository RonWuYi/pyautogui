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
    #################################################
    # wei wang ren wu
    #################################################
    # pyautogui.moveTo(1473, 388)
    # pyautogui.PAUSE = 1
    # pyautogui.click()
    # pyautogui.PAUSE = 1

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
            # pyautogui.PAUSE = 1
            # pyautogui.rightClick()
            # pyautogui.PAUSE = 3
            # pyautogui.rightClick()
            # pyautogui.PAUSE = 3
            # pyautogui.rightClick()
            # pyautogui.PAUSE = 3

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
    for iii in range(0, 10):
        moveValue = 30;
        # chuan
        pyautogui.PAUSE = 2
        # pyautogui.moveTo(1513, 345)
        pyautogui.moveTo(1512, 385)
        # 1512, 385
        pyautogui.PAUSE = 2
        pyautogui.click()
        pyautogui.PAUSE = 2

        # fu ben ming zi
        pyautogui.PAUSE = 2
        pyautogui.moveTo(801, (445 + (iii * moveValue)))
        pyautogui.PAUSE = 2
        pyautogui.PAUSE = 2

        # xia yi 10 pixels
        # pyautogui.moveRel(None, 10)
        pyautogui.click()
        pyautogui.PAUSE = 2
        pyautogui.PAUSE = 2

        # jin ru fu ben
        pyautogui.moveTo(789, 629)
        pyautogui.PAUSE = 2
        pyautogui.click()
        pyautogui.PAUSE = 2

        # zi dong zhan dou
        pyautogui.PAUSE = 2
        pyautogui.press('z')
        # # pyautogui.moveTo(1002, 703)
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 200
        # #pyautogui.PAUSE = 200
        # # pyautogui.click()
        # # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        time.sleep(200)
        pyautogui.moveTo(1435, 530)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        pyautogui.moveTo(801, 475)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(791, 627)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1002, 703)
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1432, 523)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        pyautogui.moveTo(801, 505)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(791, 627)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1002, 703)
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1432, 523)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        pyautogui.moveTo(801, 535)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(791, 627)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1002, 703)
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1432, 523)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        pyautogui.moveTo(801, 565)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(791, 627)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1002, 703)
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1432, 523)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        pyautogui.moveTo(801, 595)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(791, 627)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1002, 703)
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1432, 523)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        pyautogui.moveTo(801, 625)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(791, 627)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1002, 703)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1432, 523)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

def HuiShouWuPin():
    pyautogui.moveTo(1460, 540)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.moveTo(810, 456)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.PAUSE = 1
    pyautogui.moveTo(889, 602)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.PAUSE = 1
    pyautogui.moveTo(1092, 601)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

def GuaJi():
    # move click gua ji
    pyautogui.moveTo(1492, 575)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.moveTo(692, 465)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.press('m')
    pyautogui.PAUSE = 1
    pyautogui.moveTo(494, 367)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

def WaKuang():
    pyautogui.PAUSE = 1
    pyautogui.moveTo(1220, 611)
    pyautogui.PAUSE = 1
    time.sleep(100)
    pyautogui.click()
    pyautogui.PAUSE = 1



