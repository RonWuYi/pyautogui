import os
import subprocess
import time
import sys


from data.cuspath import CUSPATH
from data.filehash import md5

gitlabaddress = 'git@gitlab.emea.irdeto.com'
githubaddress = 'git@github.com'

bspath = "C:\\Program Files\\Git\\bin\\"
bsfilepath = "C:\\Program Files\\Git\\bin\\bash.exe"

MyPath = CUSPATH()


def isgrolupreadable(filepath):
    st = os.stat(filepath)
    return oct(st.st_mode)[-3:]


def filepermission():
    if int(isgrolupreadable(MyPath.sshpath)) > 600 and \
        int(isgrolupreadable(
                    os.path.join(MyPath.sshpath, 'id_rsa.pub'))) > 600:
    # if isgrolupreadable(MyPath.sshpath) != '700' and \
    #         isgrolupreadable(
    #                 os.path.join(MyPath.sshpath, 'id_rsa.pub')) != '600':
        return True
    else:
        return False


#def filecheck(valuesa, valuesb, osbool):
def filecheck(valuesa, valuesb):
    global checkfilemd5

    # if osbool:
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
        if gitconnectioncheck(githubaddress, CUSPATH.inlinux()):
            print('Connect to github successfully')
        else:
            print('Connect to github failed')
    elif checkfilemd5 in valuesb:
        # if checkfilemd5 in LabData.values():
        os.system('git config --global user.name "ron.wu"')
        time.sleep(1)
        os.system('git config --global user.email "ron.wu@irdeto.com"')
        time.sleep(1)
        print('git files changed to gitlab EMEA')
        if gitconnectioncheck(gitlabaddress, CUSPATH.inlinux()):
            print('Connect to gitlab successfully')
        else:
            print('Connect to gitlab failed')
    else:
        print("Switch git failed!")


def gitconnectioncheck(whichgit, osbool):
    if osbool:
        try:
            os.system('ssh-add -D')
            subprocess.check_output(["ssh", "-T", whichgit], timeout=3, stderr=subprocess.STDOUT)
            return True
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            out_bytes = e.output
            try:
                code = e.returncode
                # print(out_bytes)
                if out_bytes[0:2] == b'Hi' or out_bytes[0:7] == b'Welcome' and code == 1:
                    return True
                # print(code)
                else:
                    return False
            except AttributeError as e:
                print(e)
                return False
    else:
        if bspath not in sys.path:
            sys.path.append(bspath)

        os.system('cd {}'.format(bspath))
        try:
            cmdoutput = subprocess.check_output('{} -c "ssh -T {}"'.format(bsfilepath, whichgit), timeout=5, stderr=subprocess.STDOUT)
            if cmdoutput[0:2] == b'Hi' or cmdoutput[0:7] == b'Welcome':

                return True
                # print(code)
            else:
                return False
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            out_bytes = e.output
            try:
                code = e.returncode
                # print(out_bytes)
                if out_bytes[0:2] == b'Hi' or out_bytes[0:7] == b'Welcome' and code == 1:
                    return True
                # print(code)
                else:
                    return False
            except AttributeError as e:
                print(e)
                return False


def folder_check():
    if os.path.isdir(MyPath.sshpath):
        return True
    else:
        return False


def file_check():
    if len(os.listdir(MyPath.sshpath)) == 0:
        return False
    else:
        return True
