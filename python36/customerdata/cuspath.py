import os

from pathlib import Path
from .ftp import myftp
from .util import inlinux

class CUSPATH:
    def __init__(self, gitlabpath = None,
                 githubpath = None, sshpath = None,
                 gitkey = None):
        self.gitlabpath = gitlabpath
        self.githubpath = githubpath
        self.sshpath = sshpath
        self.gitkey = gitkey
        self.ospath(inlinux())

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
        # if inlinux:
        if not os.path.exists(self.sshpath):
            myftp(str(Path.home()))

                # if self.sshpath


    def oscheck(self, ):
        if not os.path.isfile(self.gitkey):
            for file in os.listdir(self.githubpath):
                os.system('cp -f {} {}'.format(os.path.join(self.githubpath, file), self.sshpath))
        else:
            pass
        # if inlinux:
        #     self.gitlabpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('gitlab'))
        #     self.githubpath = os.path.join(str(Path.home()), '.ssh/{}/'.format('github'))
        #     self.sshpath = os.path.join(str(Path.home()), '.ssh/')
        #
        #     if os.path.exists(self.sshpath):
        #         if not os.path.isfile(os.path.join(self.sshpath, 'id_rsa.pub')):
        #             for file in os.listdir(self.githubpath):
        #                 os.system('cp -f {} {}'.format(os.path.join(self.githubpath, file), self.sshpath))
        #     else:
        #         # try:
        #         os.system('cd ~/')
                # except
        # else:
        #
        #     self.gitlabpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('gitlab'))
        #     self.githubpath = os.path.join(str(Path.home()), '.ssh\\{}\\'.format('github'))
        #     self.sshpath = os.path.join(str(Path.home()), '.ssh\\')
        #
        #     if os.path.exists(self.sshpath):
        #         print('~/.ssh/ exist')
        #         if not os.path.isfile(os.path.join(self.sshpath, 'id_rsa.pub')):
        #             for file in os.listdir(self.githubpath):
        #                 os.system('cp -f {} {}'.format(os.path.join(self.githubpath, file), self.sshpath))
        #     else:
        #         print('~/.ssh/ does not exist or git ssh key file not in default folder')
