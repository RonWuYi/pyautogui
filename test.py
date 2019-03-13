# from data.cuspath import *
from data.ftp import *
from ftplib import FTP

ftp = FTP('172.16.66.149', 5)

print(ftp)
# mypath = CUSPATH()
# mypath.rootpathcheck()