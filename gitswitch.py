import shutil

from data.util import *
from data.const import *


def run():
    rootpathcheck()

    for x, y, z in sshpath:
        if len(z) > 0 and hubjson in z and labjson in z:
            githubjson = loadjson(sshpath, os.path.join(sshpath, hubjson))
            gitlabjson = loadjson(sshpath, os.path.join(sshpath, labjson))

            if inlinux():
                if md5(gitkey) in gitlabjson:
                    for file in os.listdir(githubpath):
                        os.system('cp -f {} {}'.format(os.path.join(githubpath, file), sshpath))
                else:
                    for file in os.listdir(gitlabpath):
                        os.system('cp -f {} {}'.format(os.path.join(gitlabpath, file), sshpath))

                if not filepermission():
                    os.system('chmod 0600 {}'.format(sshpath))
                    time.sleep(1)
                    os.system('chmod 0600 {}'.format(os.path.join(sshpath, 'id_rsa.pub')))
                    time.sleep(1)
                    os.system('chmod 0600 {}'.format(os.path.join(sshpath, 'id_rsa')))
            else:
                if md5(gitkey) in githubjson:
                    for file in os.listdir(githubpath):
                        shutil.copy(os.path.join(githubpath, file), sshpath)
                else:
                    for file in os.listdir(gitlabpath):
                        shutil.copy(os.path.join(gitlabpath, file), sshpath)
            filecheck(gitlabjson, githubjson)
        else:
            if inlinux():
                if md5(gitkey) in gitlabjson:
                    for file in os.listdir(githubpath):
                        os.system('cp -f {} {}'.format(os.path.join(githubpath, file), sshpath))
                else:
                    for file in os.listdir(gitlabpath):
                        os.system('cp -f {} {}'.format(os.path.join(gitlabpath, file), sshpath))

                if not filepermission():
                    os.system('chmod 0600 {}'.format(sshpath))
                    time.sleep(1)
                    os.system('chmod 0600 {}'.format(os.path.join(sshpath, 'id_rsa.pub')))
                    time.sleep(1)
                    os.system('chmod 0600 {}'.format(os.path.join(sshpath, 'id_rsa')))
            else:
                if md5(gitkey) in githubjson:
                    for file in os.listdir(githubpath):
                        shutil.copy(os.path.join(githubpath, file), sshpath)
                else:
                    for file in os.listdir(gitlabpath):
                        shutil.copy(os.path.join(gitlabpath, file), sshpath)



if __name__ == '__main__':
    run()
