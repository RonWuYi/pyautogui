import os
import zipfile
import platform

from pathlib import Path
from .ftp import myftp, mydropbox, internet_on


class CUSPATH:
    def __init__(self, gitlabpath=None,
                 githubpath=None, sshpath=None,
                 gitkey=None):
        # self.osbool = inlinux()
        self.gitlabpath = gitlabpath
        self.githubpath = githubpath
        self.sshpath = sshpath
        self.gitkey = gitkey
        # self.ospath(inlinux())
        self.ospath(CUSPATH.inlinux())
        # self.rootpathcheck()

    # def ospath(self):
    #     if CUSPATH.inlinux():
    #         self.gitlabpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('gitlab'))
    #         self.githubpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('github'))
    #         self.sshpath = os.path.join(str(Path.home()), '.ssh/')
    #     else:
    #         self.gitlabpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('gitlab'))
    #         self.githubpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('github'))
    #         self.sshpath = os.path.join(str(Path.home()), '.ssh\\')
    #
    #     self.gitkey = os.path.join(self.sshpath, 'id_rsa.pub')

    @classmethod
    def ospath(cls, os):
        if os:
            cls().gitlabpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('gitlab'))
            cls().githubpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('github'))
            cls().sshpath = os.path.join(str(Path.home()), '.ssh/')
        else:
            cls().gitlabpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('gitlab'))
            cls().githubpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('github'))
            cls().sshpath = os.path.join(str(Path.home()), '.ssh\\')

        cls().gitkey = os.path.join(cls().sshpath, 'id_rsa.pub')

    @classmethod
    def rootpathcheck(cls):
        if not os.path.exists(cls().sshpath):
            if internet_on():
                mydropbox()
                if os.path.isfile(os.path.join((str(Path.home())), 'ssh.zip')):
                    zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
                    zip_ref.extractall(path=cls().sshpath)
                    zip_ref.close()
                    os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
                else:
                    print("get file from dropbox failed")
            elif myftp(str(Path.home())):
                # myftp(str(Path.home()))
                zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
                zip_ref.extractall(path=cls().sshpath)
                zip_ref.close()
                os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
            else:
                print("either cannot connect to Interent or cannot connect to ftp")
        elif len(os.listdir(cls().sshpath)) == 0:
            if internet_on():
                mydropbox()
                if os.path.isfile(os.path.join((str(Path.home())), 'ssh.zip')):
                    zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
                    zip_ref.extractall(path=cls().sshpath)
                    zip_ref.close()
                    os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
                else:
                    print("get file from dropbox failed")
            elif myftp(str(Path.home())):
                # myftp(str(Path.home()))
                zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
                zip_ref.extractall(path=cls().sshpath)
                zip_ref.close()
                os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
            else:
                print("either cannot connect to Interent or cannot connect to ftp")
        else:
            print('id_rsa.pub file already exist')

    @staticmethod
    def inlinux():
        if platform.system() == 'Linux':
            return True
        else:
            return False
