import os
import platform
import zipfile

from pathlib import Path
from .ftp import internet_on, mydropbox, myftp

gitlabpath = os.path.join(Path.home(), '.ssh', 'gitlab')
githubpath = os.path.join(Path.home(), '.ssh', 'github')
sshpath = os.path.join(Path.home(), '.ssh')
gitkey = os.path.join(sshpath, 'id_rsa.pub')

gitlabaddress = 'git@gitlab.emea.irdeto.com'
githubaddress = 'git@github.com'
hubjson = 'github.json'
labjson = 'gitlab.json'


bsPath_win = "C:\\Program Files\\Git\\bin\\"
bsFilePath_win = "C:\\Program Files\\Git\\bin\\bash.exe"


def inlinux():
    if platform.system() == 'Linux':
        return True
    else:
        return False


def rootpathcheck() -> None:
    if not os.path.exists(sshpath):
        if internet_on():
            mydropbox()
            if os.path.isfile(os.path.join((str(Path.home())), 'ssh.zip')):
                zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
                zip_ref.extractall(path=sshpath)
                zip_ref.close()
                os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
            else:
                print("get file from dropbox failed")
        elif myftp(str(Path.home())):
            zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
            zip_ref.extractall(path=sshpath)
            zip_ref.close()
            os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
        else:
            print("either cannot connect to Interent or cannot connect to ftp")
    elif len(os.listdir(sshpath)) == 0:
        if internet_on():
            mydropbox()
            if os.path.isfile(os.path.join((str(Path.home())), 'ssh.zip')):
                zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
                zip_ref.extractall(path=sshpath)
                zip_ref.close()
                os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
            else:
                print("get file from dropbox failed")
        elif myftp(str(Path.home())):
            zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
            zip_ref.extractall(path=sshpath)
            zip_ref.close()
            os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
        else:
            print("either cannot connect to Interent or cannot connect to ftp")
    else:
        print('id_rsa.pub file already exist')


if __name__ == '__main__':
    print(sshpath)
