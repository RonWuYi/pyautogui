import hashlib
import os
import json
import time
import platform
import subprocess

gitpath = "C:\\Program Files\\Git\\bin\\bash.exe"

gitlabpath = '/home/hdc/.ssh/gitlab/'
githubpath = '/home/hdc/.ssh/github/'
sshpath = '/home/hdc/.ssh/'

gitlabaddress = 'git@gitlab.emea.irdeto.com'
githubaddress = 'git@github.com'


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    # for chunk in iter(lambda: fname.open.read(4096), b""):
    #     hash_md5.update(chunk)
    # fname.close()
    return hash_md5.hexdigest()


def isgrolupreadable(filepath):
    st = os.stat(filepath)
    return oct(st.st_mode)[-3:]


def filepermission():
    if isgrolupreadable(sshpath) != '700' and \
            isgrolupreadable(
                    os.path.join(sshpath, 'id_rsa.pub')) != '600':
        return False
    else:
        return True


def inlinux():
    if platform.system() == 'Linux':
        return True
    else:
        return False


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


LabData = {}
HubData = {}
filemd5 = None
checkfilemd5 = None

# todo: implemented it
# if InLinux():
#     if os.path.exists(sshpath):
#         if not os.path.isfile(os.path.join(sshpath, 'id_rsa.pub')):
#             for file in os.listdir(githubpath):
#                 os.system('cp -f {} {}'.format(os.path.join(githubpath, file), sshpath))
# else:
#     obj = subprocess.Popen([gitpath], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                            universal_newlines=True)
#
#     out_error_list = obj.communicate('cd ~/.ssh/')
#     if out_error_list[1] == '':
#         print('~/.ssh/ exist')
#     else:
#         print('~/.ssh/ does not exist or git ssh key file not in default folder')


for files in os.listdir(sshpath):
    if len(files) > 0:
        if files == 'gitlab.json':
            with open(os.path.join(sshpath, files), 'r') as f:
                LabData = json.load(f)
            break
    else:
        print("no file stored at {}.".format(sshpath))


for files in os.listdir(sshpath):
    if len(files) > 0:
        if files == 'github.json':
            with open(os.path.join(sshpath, files), 'r') as f:
                HubData = json.load(f)
            break
        # else:
        #     print("cannot file json file.")
    else:
        print("no file stored at {}.".format(sshpath))

    # else:
    #     print("no json data loaded!")

for files in os.listdir(sshpath):
    if files == 'id_rsa.pub':
        filemd5 = md5(os.path.join(sshpath, files))
        break

if filemd5 in LabData.values():
    for file in os.listdir(githubpath):
        os.system('cp -f {} {}'.format(os.path.join(githubpath, file), sshpath))

    for files in os.listdir(sshpath):
        if files == 'id_rsa.pub':
            checkfilemd5 = md5(os.path.join(sshpath, files))
            break

    if inlinux():
        if not filepermission():
            os.system('chmod 700 {}'.format(sshpath))
            time.sleep(1)
            os.system('chmod 600 {}'.format(os.path.join(sshpath, 'id_rsa.pub')))
            time.sleep(1)
            os.system('chmod 600 {}'.format(os.path.join(sshpath, 'id_rsa')))
    if checkfilemd5 in HubData.values():
        os.system('git config --global user.name "RonWuYi"')
        time.sleep(1)
        os.system('git config --global user.email "lyshmily@outlook.com"')
        time.sleep(1)
        print('git files changed to github Internet')
        if gitconnectioncheck(githubaddress):
            print('change to git hub success')
        else:
            print('failed change to git hub')
    else:
        print("Switch to github Internet failed!")
else:
    for file in os.listdir(gitlabpath):
        os.system('cp -f {} {}'.format(os.path.join(gitlabpath, file), sshpath))

    for files in os.listdir(sshpath):
        if files == 'id_rsa.pub':
            checkfilemd5 = md5(os.path.join(sshpath, files))
            break

    if inlinux():
        if not filepermission():
            os.system('chmod 700 {}'.format(sshpath))
            time.sleep(1)
            os.system('chmod 600 {}'.format(os.path.join(sshpath, 'id_rsa.pub')))
            time.sleep(1)
            os.system('chmod 600 {}'.format(os.path.join(sshpath, 'id_rsa')))

    if checkfilemd5 in LabData.values():
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
        print("Switch to gitlab EMEA failed!")
