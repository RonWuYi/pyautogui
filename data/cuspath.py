import os
import zipfile
import platform

from pathlib import Path
from .ftp import myftp


class CUSPATH:
    def __init__(self, gitlabpath=None,
                 githubpath=None, sshpath=None,
                 gitkey=None):
        self.gitlabpath = gitlabpath
        self.githubpath = githubpath
        self.sshpath = sshpath
        self.gitkey = gitkey
        self.ospath(CUSPATH.inlinux())

    def ospath(self, inlinux):
        if inlinux:
            self.gitlabpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('gitlab'))
            self.githubpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('github'))
            self.sshpath = os.path.join(str(Path.home()), '.ssh/')
        else:
            self.gitlabpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('gitlab'))
            self.githubpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('github'))
            self.sshpath = os.path.join(str(Path.home()), '.ssh\\')

        self.gitkey = os.path.join(self.sshpath, 'id_rsa.pub')

    def rootpathcheck(self):
        if not os.path.exists(self.sshpath):
            myftp(str(Path.home()))
            zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
            zip_ref.extractall(path=self.sshpath)
            zip_ref.close()
            os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
        else:
            print('id_rsa.pub file already exist')

    @staticmethod
    def inlinux():
        if platform.system() == 'Linux':
            return True
        else:
            return False
