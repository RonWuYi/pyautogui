import os
import re


print(os.path.dirname(__file__))
print(type(os.path.dirname(__file__)))

print(os.getcwd())

print(type(os.getcwd()))


import subprocess
import sys

from subprocess import Popen
p = subprocess.Popen(["powershell.exe","-ExecutionPolicy", "Bypass", "-File",
                    os.path.join(os.path.dirname(__file__), "odversion.ps1")],
                    stdout=sys.stdout)
p.communicate()

p.kill()


with open(os.path.join(os.path.dirname(__file__), "output.txt")) as f:
    for i in f.readlines():
        if i.startswith('Name'):

            print(i)



# with Popen(["powershell.exe",
#                     os.path.join(os.path.dirname(__file__), "odversion.ps1")]) as proc:
#                     proc.terminate()
#                     # print(proc.stdout.read())



