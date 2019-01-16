import json
import time

from python36.customerdata.util import *


class SWITCH:
    @staticmethod
    def run():
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


if __name__ == '__main__':
    SWITCH.run()
