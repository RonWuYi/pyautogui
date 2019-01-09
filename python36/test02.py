import os
import platform
# import stat

print(platform.system())

myfilepath = '/home/hdc/PycharmProjects/untitled1/github.json'
test02file = '/home/hdc/PycharmProjects/untitled1/test02.py'


def isgrolupreadable(filepath):
    st = os.stat(filepath)
    return oct(st.st_mode)


st = os.stat(test02file)
oct_perm = oct(st.st_mode)
print(oct_perm)
print(oct_perm[-3:])

print(isgrolupreadable(test02file))


print(isgrolupreadable(myfilepath))