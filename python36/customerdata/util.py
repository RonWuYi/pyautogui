import hashlib
import os
import platform
import subprocess
import time

from python36.customerdata.cuspath import CUSPATH
from python36.customerdata.ftp import myftp
from .filehash import md5
# gitpath = "C:\\Program Files\\Git\\bin\\bash.exe"

# gitlabpath = '/home/hdc/.ssh/gitlab/'
# githubpath = '/home/hdc/.ssh/github/'
# sshpath = '/home/hdc/.ssh/'

gitlabaddress = 'git@gitlab.emea.irdeto.com'
githubaddress = 'git@github.com'

# filemd5 = None
# checkfilemd5 = None
MyPath = CUSPATH()


def isgrolupreadable(filepath):
    st = os.stat(filepath)
    return oct(st.st_mode)[-3:]


def filepermission():
    if isgrolupreadable(MyPath.sshpath) != '700' and \
            isgrolupreadable(
                    os.path.join(MyPath.sshpath, 'id_rsa.pub')) != '600':
        return False
    else:
        return True


def inlinux():
    if platform.system() == 'Linux':
        return True
    else:
        return False


def filecheck(valuesa, valuesb):
    global checkfilemd5

    for files in os.listdir(MyPath.sshpath):
        if files == 'id_rsa.pub':
            checkfilemd5 = md5(os.path.join(MyPath.sshpath, files))

    # if checkfilemd5 in HubData.values():
    if checkfilemd5 in valuesa:
        os.system('git config --global user.name "RonWuYi"')
        time.sleep(1)
        os.system('git config --global user.email "lyshmily@outlook.com"')
        time.sleep(1)
        print('git files changed to github Internet')
        if gitconnectioncheck(githubaddress):
            print('change to git hub success')
        else:
            print('failed change to git hub')
    elif checkfilemd5 in valuesb:
        # if checkfilemd5 in LabData.values():
        os.system('git config --global user.name "ron.wu"')
        time.sleep(1)
        os.system('git config --global user.email "ron.wu@irdeto.com"')
        time.sleep(1)
        print('git files changed to gitlab EMEA')
        if gitconnectioncheck(gitlabaddress):
            print('change to git lab success')
        else:
            print('failed change to git lab')
    else:
        print("Switch git failed!")


def gitconnectioncheck(whichgit):
    try:
        os.system('ssh-add -D')
        subprocess.check_output(["ssh", "-T", whichgit], timeout=3, stderr=subprocess.STDOUT)
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        out_bytes = e.output
        try:
            code = e.returncode
            # print(out_bytes)
            if out_bytes[0:2] == b'Hi' and code == 1:
                return True
            # print(code)
            else:
                return False
        except AttributeError as e:
            print(e)
            return False