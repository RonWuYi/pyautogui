import os
import platform
import stat

print(platform.system())

myfilepath = '/home/hdc/PycharmProjects/untitled1/github.json'


def isgrolupreadable(filepath):
    st = os.stat(filepath)
    return bool(st.st_mode & stat.S_IRGRP)

st = os.stat(myfilepath)
oct_perm = oct(st.st_mode)
print(oct_perm)


print(isgrolupreadable(myfilepath))