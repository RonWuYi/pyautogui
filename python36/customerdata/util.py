import hashlib
import os
import platform
import subprocess

gitpath = "C:\\Program Files\\Git\\bin\\bash.exe"

gitlabpath = '/home/hdc/.ssh/gitlab/'
githubpath = '/home/hdc/.ssh/github/'
sshpath = '/home/hdc/.ssh/'

gitlabaddress = 'git@gitlab.emea.irdeto.com'
githubaddress = 'git@github.com'

LabData = {}
HubData = {}
filemd5 = None
checkfilemd5 = None

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
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


