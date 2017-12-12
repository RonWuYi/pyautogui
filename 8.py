from AllWay import *
import time

# TabQieHuan()
# TianFu()
# CaiLiaoFuBen()
# JinYanGongXun()

print str(time.localtime()[3])+str(time.localtime()[4])

while True:
    time.sleep(5)
    if (str(time.localtime()[3])+str(time.localtime()[4])=='1259'):
        print "launch time"
        print "***************************************************"
        GuaJi()
    else:
        print "continue move fomrward"
        print "current time is " + str(time.localtime()[3]) + str(time.localtime()[4])
        print "###################################################"