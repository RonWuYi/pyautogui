import pyautogui

# pyautogui.PAUSE = 1

try:
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
except:
    print "except"

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


#clict "jie shou ren wu"/" qu wan cheng ren wu"
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
    pyautogui.PAUSE = 140

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

#################################################
# tian fu
#################################################

#chuan
pyautogui.moveTo(1522, 345)
pyautogui.PAUSE = 1
pyautogui.click()
pyautogui.PAUSE = 1

# clict "jie shou ren wu"/" qu wan cheng ren wu"
pyautogui.moveTo(800, 612)
pyautogui.PAUSE = 2
pyautogui.click()
pyautogui.PAUSE = 3
pyautogui.click()
pyautogui.PAUSE = 240

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
    pyautogui.PAUSE = 240

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


#################################################
# wei wang ren wu
#################################################
# pyautogui.moveTo(1473, 388)
# pyautogui.PAUSE = 1
# pyautogui.click()
# pyautogui.PAUSE = 1

#################################################
# ta fang jing yan
#################################################
for jj in range(4):
    # pyautogui.moveTo(1505, 422)
    pyautogui.moveTo(1505, 462)
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
# # dao lu dian ji dian
# pyautogui.moveTo(1300, 410)

#################################################
# cai liao fu ben
#################################################
for iii in range(2):
    pyautogui.PAUSE = 1
    pyautogui.moveTo(1513, 385)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1

    pyautogui.PAUSE = 1
    pyautogui.moveTo(801, 445)
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



#################################################
# gua ji
#################################################

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