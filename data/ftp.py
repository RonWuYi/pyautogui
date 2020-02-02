import os
import urllib.request
from subprocess import Popen, PIPE

from pathlib import Path
from ftplib import FTP

file_url = "https://www.dropbox.com/s/0wvwp5fc521liae/ssh.zip"

def myftp(path):
    try:
        ftp = FTP('172.16.66.149', 5)
    except (ConnectionResetError, ConnectionRefusedError, ConnectionError, ConnectionAbortedError) as e:
        print(e)
        return
    ftp.login('anonymous', '123')
    files = ftp.nlst()
    for file in files:
        if file == 'ssh.zip':
            ftp.retrbinary("RETR " + file, open(os.path.join(path, file), 'wb').write)
    ftp.close()


def mydropbox() -> None:
    try:
        os.chdir(str(Path.home()))
    except OSError as e:
        print(e)
    try:
        # os.system("wget https://www.dropbox.com/s/0wvwp5fc521liae/ssh.zip")
        p = Popen(["powershell.exe", "wget", file_url], stdout=PIPE)
        p.communicate()
    except Exception as e:
        print(e)
        # return


def internet_on() -> bool:
    try:
        urllib.request.urlopen('https://www.google.com/', timeout=1)
        return True
    except Exception as err:
        return False
