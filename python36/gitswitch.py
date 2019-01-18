from python36.customerdata.util import *
from python36.customerdata.cuspath import CUSPATH
from python36.customerdata.filehash import filehash

MyPath = CUSPATH()
curfilehas = filehash()

class SWITCH:
    @staticmethod
    def run():
        if curfilehas.filemd5 in curfilehas.LabData.values():
            for file in os.listdir(MyPath.githubpath):
                os.system('cp -f {} {}'.format(os.path.join(MyPath.githubpath, file), MyPath.sshpath))

            if inlinux():
                if not filepermission():
                    os.system('chmod 700 {}'.format(MyPath.sshpath))
                    time.sleep(1)
                    os.system('chmod 600 {}'.format(os.path.join(MyPath.sshpath, 'id_rsa.pub')))
                    time.sleep(1)
                    os.system('chmod 600 {}'.format(os.path.join(MyPath.sshpath, 'id_rsa')))
            else:
                print("Switch to github Internet failed!")
        else:
            for file in os.listdir(MyPath.gitlabpath):
                os.system('cp -f {} {}'.format(os.path.join(MyPath.gitlabpath, file), MyPath.sshpath))

            if inlinux():

                if not filepermission():
                    os.system('chmod 700 {}'.format(MyPath.sshpath))
                    time.sleep(1)
                    os.system('chmod 600 {}'.format(os.path.join(MyPath.sshpath, 'id_rsa.pub')))
                    time.sleep(1)
                    os.system('chmod 600 {}'.format(os.path.join(MyPath.sshpath, 'id_rsa')))
            else:
                print("Switch to gitlab EMEA failed!")

        filecheck(curfilehas.HubData.values(), curfilehas.LabData.values())


if __name__ == '__main__':
    SWITCH.run()
