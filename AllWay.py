import pyautogui
import time

def TabQieHuan():
    pyautogui.PAUSE = 1
    try:
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    except:
        print "except"

def JinYanGongXun():
    #################################################
    # jin yan gong xun
    #################################################
    # for i in range(1):
    # click "chuan"
    pyautogui.PAUSE = 1
    pyautogui.moveTo(1508, 345)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

    # clict "shua xin"
    pyautogui.moveTo(910, 570)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 9

    # clict "jie shou ren wu"/" qu wan cheng ren wu"
    pyautogui.moveTo(800, 612)
    pyautogui.PAUSE = 2
    pyautogui.click()
    pyautogui.PAUSE = 3
    pyautogui.click()
    pyautogui.PAUSE = 100

    # #######################################################
    # # # # click gua ji
    # # pyautogui.moveTo(1003, 705)
    # # pyautogui.PAUSE = 0.5
    # # pyautogui.click()
    # # pyautogui.PAUSE = 70.9
    # #################################################################
    # click "chuan"
    pyautogui.moveTo(1480, 345)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

    # click "san bei jiang li"
    pyautogui.moveTo(900, 555)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

    for i in range(9):
        # clict "shua xin"
        pyautogui.moveTo(910, 570)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 12

        # clict "jie shou ren wu"/" qu wan cheng ren wu"
        pyautogui.moveTo(800, 612)
        pyautogui.PAUSE = 2
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        time.sleep(150)
        # pyautogui.PAUSE = 140

        # click "chuan"
        pyautogui.moveTo(1480, 345)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        # click "san bei jiang li"
        pyautogui.moveTo(900, 555)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

def TianFu():
    #################################################
    # tian fu
    #################################################

    # chuan
    pyautogui.moveTo(1519, 345)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

    # clict "jie shou ren wu"/" qu wan cheng ren wu"
    pyautogui.moveTo(800, 612)
    pyautogui.PAUSE = 2
    pyautogui.click()
    pyautogui.PAUSE = 3
    pyautogui.click()
    time.sleep(240)
    # pyautogui.PAUSE = 240

    # chuan
    pyautogui.moveTo(1474, 345)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

    # click "san bei jiang li"
    pyautogui.moveTo(900, 555)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

    for j in range(9):
        # clict "jie shou ren wu"/" qu wan cheng ren wu"
        pyautogui.moveTo(800, 612)
        pyautogui.PAUSE = 2
        pyautogui.click()
        pyautogui.PAUSE = 3
        pyautogui.click()
        time.sleep(240)
        # pyautogui.PAUSE = 240

        # chuan
        pyautogui.moveTo(1474, 345)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        # click "san bei jiang li"
        pyautogui.moveTo(900, 555)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

def WeiWangRenWu():
    pass
    #################################################
    # wei wang ren wu
    #################################################
    # pyautogui.moveTo(1473, 388)
    # pyautogui.PAUSE = 1
    # pyautogui.click()
    # pyautogui.PAUSE = 1

def TaFangJingYan():
    #################################################
    # ta fang jing yan
    #################################################
    for jj in range(4):
        # pyautogui.moveTo(1505, 422)
        pyautogui.moveTo(1519, 349)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        # jin ru feng mo gu
        pyautogui.moveTo(790, 635)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        # kai shi shua guai
        pyautogui.moveTo(990, 545)
        pyautogui.PAUSE = 1
        pyautogui.click()
        pyautogui.PAUSE = 1

        for ii in range(2):
            # dian
            pyautogui.moveTo(610, 545)
            pyautogui.PAUSE = 1
            pyautogui.click()
            pyautogui.PAUSE = 1

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.PAUSE = 1
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3

            # du
            pyautogui.moveTo(700, 545)
            pyautogui.PAUSE = 1
            pyautogui.click()
            pyautogui.PAUSE = 1

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.PAUSE = 1
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3

            # bin
            pyautogui.moveTo(800, 545)
            pyautogui.PAUSE = 1
            pyautogui.click()
            pyautogui.PAUSE = 1

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.PAUSE = 1
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3

            # bao
            pyautogui.moveTo(890, 545)
            pyautogui.PAUSE = 1
            pyautogui.click()
            pyautogui.PAUSE = 1

            # dao lu dian ji dian, ren wu qian jin
            pyautogui.moveTo(1300, 410)
            pyautogui.PAUSE = 1
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3
            pyautogui.rightClick()
            pyautogui.PAUSE = 3

            # deng dai jie shu
            pyautogui.PAUSE = 500
            # pyautogui.moveTo(990, 545)

            # lin qu jiang li
            pyautogui.moveTo(900, 425)
            pyautogui.PAUSE = 1
            pyautogui.click()
            pyautogui.PAUSE = 1
            # # dao lu dian ji dian
            # pyautogui.moveTo(1300, 410)

def CaiLiaoFuBen():
    #################################################
    # cai liao fu ben
    #################################################
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

        # pyautogui.moveTo(801, 475)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(791, 627)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1002, 703)
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1432, 523)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        #
        # pyautogui.moveTo(801, 505)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(791, 627)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1002, 703)
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1432, 523)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        #
        # pyautogui.moveTo(801, 535)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(791, 627)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1002, 703)
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1432, 523)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        #
        # pyautogui.moveTo(801, 565)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(791, 627)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1002, 703)
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1432, 523)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        #
        # pyautogui.moveTo(801, 595)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(791, 627)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1002, 703)
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1432, 523)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        #
        # pyautogui.moveTo(801, 625)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(791, 627)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1002, 703)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1
        # pyautogui.PAUSE = 1
        # pyautogui.moveTo(1432, 523)
        # pyautogui.PAUSE = 1
        # pyautogui.click()
        # pyautogui.PAUSE = 1

def HuiShou():
    #################################################
    # hui shou
    #################################################
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



