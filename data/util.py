import subprocess
import time
import sys
import json
import hashlib

from .const import *
from subprocess import call


def isgrolupreadable(filepath):
    st = os.stat(filepath)
    return oct(st.st_mode)[-3:]


def filepermission():
    if int(isgrolupreadable(sshpath)) > 600 and \
        int(isgrolupreadable(
                    os.path.join(sshpath, 'id_rsa.pub'))) > 600:
        return True
    else:
        return False


def filecheck(labvalues, hubvalues):
    checkfilemd5 = md5(os.path.join(gitkey))

    if checkfilemd5 in hubvalues:
        os.system('git config --global user.name "RonWuYi"')
        time.sleep(1)
        os.system('git config --global user.email "lyshmily@outlook.com"')
        time.sleep(1)
        print('git files changed to github Internet')
        # if gitconnectioncheck(githubaddress, inlinux()):
        #     print('Connect to github successfully')
        # else:
        #     print('Connect to github failed')
    elif checkfilemd5 in labvalues:
        os.system('git config --global user.name "ron.wu"')
        time.sleep(1)
        os.system('git config --global user.email "ron.wu@irdeto.com"')
        time.sleep(1)
        print('git files changed to gitlab EMEA')
        # if gitconnectioncheck(gitlabaddress, inlinux()):
        #     print('Connect to gitlab successfully')
        # else:
        #     print('Connect to gitlab failed')
    else:
        print("Switch git failed, cannot find hash key form json libray!")


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
        if bsPath_win not in sys.path:
            sys.path.append(bsPath_win)

        os.system('cd {}'.format(bsPath_win))
        try:
            cmdoutput = subprocess.check_output('{} -c "ssh -T {}"'.format(bsFilePath_win, whichgit), timeout=5, stderr=subprocess.STDOUT)
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

    if gitconnectioncheck(githubaddress, inlinux()):
        print('Connect to github successfully')
    else:
        print('Connect to github failed')


def folder_check():
    if os.path.isdir(sshpath):
        return True
    else:
        return False


def file_check():
    if len(os.listdir(sshpath)) == 0:
        return False
    else:
        return True


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def createjson(folder1, folder2, json_file):
    # if os.path.isdir(folder):
    #     for x, y, z in os.walk(folder):
    #         if len(z) > 0 and json_file in z:
    #             with open(json_file, 'w') as f:
    #                 return json.load(f)
    #         else:
    #             print("no json file stored at {}.".format(sshpath))
    my_dict = {}
    for x, y, z in os.walk(folder1):
        if len(z) > 0:
            for i in z:
                my_dict[i] = md5(os.path.join(x, i))

    with open(os.path.join(folder2, json_file), 'w') as f:
        json.dump(my_dict, f)


def loadjson(folder, file):
    if os.path.isfile(os.path.join(folder, file)):
        with open(file, 'r') as f:
            return json.load(f)


def loadhubjson():
    if os.path.isdir(sshpath):
        for files in os.listdir(sshpath):
            if len(files) > 0:
                if files == 'github.json':
                    with open(os.path.join(sshpath, files), 'r') as f:
                        return json.load(f)
            else:
                print("no json file stored at {}.".format(sshpath))
    else:
        os.makedirs(sshpath)
        print("no ssh file at {}.".format(sshpath))


def currentfile():
    if os.path.isdir(sshpath):
        if len(os.listdir(sshpath))>0:
            for files in os.listdir(sshpath):
                if files == 'id_rsa.pub':
                    return md5(os.path.join(sshpath, files))
        else:
            print('no rsa key file and folder')
    else:
        print('no rsa key file and folder')


def changePermission(folder):
    somecommand1 = 'chmod 0777 {}'.format(folder)
    pwd = 'a'
    call('echo {} | sudo -S {}'.format(pwd, somecommand1), shell=True)
    # os.popen("sudo -S {}".format(somecommand1), 'w').write("a")
    # subprocess.Popen(somecommand1, stdin=PIPE).communicate()

    for x, y, z in os.walk(folder):
        if len(z) > 0:
            for i in z:
                somecommand2 = 'chmod 0777 {}'.format(os.path.join(x, i))
                # pwd = 'a'
                call('echo {} | sudo -S {}'.format(pwd, somecommand2), shell=True)

