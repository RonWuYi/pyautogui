import shutil

from data.util import *
from data.cuspath import CUSPATH
from data.filehash import filehash

MyPath = CUSPATH()
curfilehas = filehash()


class SWITCH:
    @staticmethod
    def run():
        MyPath.rootpathcheck()
        if CUSPATH.inlinux():
            if curfilehas.filemd5 in curfilehas.LabData.values():
                for file in os.listdir(MyPath.githubpath):
                    os.system('cp -f {} {}'.format(os.path.join(MyPath.githubpath, file), MyPath.sshpath))
            else:
                for file in os.listdir(MyPath.gitlabpath):
                    os.system('cp -f {} {}'.format(os.path.join(MyPath.gitlabpath, file), MyPath.sshpath))

            if not filepermission():
                os.system('chmod 0600 {}'.format(MyPath.sshpath))
                time.sleep(1)
                os.system('chmod 0600 {}'.format(os.path.join(MyPath.sshpath, 'id_rsa.pub')))
                time.sleep(1)
                os.system('chmod 0600 {}'.format(os.path.join(MyPath.sshpath, 'id_rsa')))
        else:
            if curfilehas.filemd5 in curfilehas.LabData.values():
                for file in os.listdir(MyPath.githubpath):
                    shutil.copy(os.path.join(MyPath.githubpath, file), MyPath.sshpath)
            else:
                for file in os.listdir(MyPath.gitlabpath):
                    shutil.copy(os.path.join(MyPath.gitlabpath, file), MyPath.sshpath)

        filecheck(curfilehas.HubData.values(), curfilehas.LabData.values())


if __name__ == '__main__':
    SWITCH.run()
