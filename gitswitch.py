import shutil

from data.util import *
from data.cuspath import CUSPATH
from data.fash import FASH

# MyPath = CUSPATH()
curfilehas = FASH()


class SWITCH:
    @staticmethod
    def run():
        CUSPATH.rootpathcheck()
        if CUSPATH.inlinux():
            if curfilehas.filemd5 in curfilehas.LabData:
                for file in os.listdir(CUSPATH.githubpath):
                    os.system('cp -f {} {}'.format(os.path.join(CUSPATH.githubpath, file), CUSPATH.sshpath))
            else:
                for file in os.listdir(CUSPATH.gitlabpath):
                    os.system('cp -f {} {}'.format(os.path.join(CUSPATH.gitlabpath, file), CUSPATH.sshpath))

            if not filepermission():
                os.system('chmod 0600 {}'.format(CUSPATH.sshpath))
                time.sleep(1)
                os.system('chmod 0600 {}'.format(os.path.join(CUSPATH.sshpath, 'id_rsa.pub')))
                time.sleep(1)
                os.system('chmod 0600 {}'.format(os.path.join(CUSPATH.sshpath, 'id_rsa')))
        else:
            if curfilehas.filemd5 in curfilehas.LabData:
                for file in os.listdir(CUSPATH.githubpath):
                    shutil.copy(os.path.join(CUSPATH.githubpath, file), CUSPATH.sshpath)
            else:
                for file in os.listdir(CUSPATH.gitlabpath):
                    shutil.copy(os.path.join(CUSPATH.gitlabpath, file), CUSPATH.sshpath)
        filecheck(curfilehas.LabData, curfilehas.HubData)


if __name__ == '__main__':
    SWITCH.run()
