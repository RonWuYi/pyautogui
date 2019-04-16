import shutil

from data.util import *
from data.const import *


def run():
    for x, y, z in os.walk(sshpath):
        if len(z) > 0 and hubjson in z and labjson in z and os.path.exists(githubpath):
            githubjson = loadjson(sshpath, os.path.join(sshpath, hubjson))
            gitlabjson = loadjson(sshpath, os.path.join(sshpath, labjson))
            if inlinux():
                if md5(gitkey) in gitlabjson.values():
                    for file in os.listdir(githubpath):
                        os.system('cp -f {} {}'.format(os.path.join(githubpath, file), sshpath))
                else:
                    for file in os.listdir(gitlabpath):
                        os.system('cp -f {} {}'.format(os.path.join(gitlabpath, file), sshpath))
            else:
                if md5(gitkey) in githubjson.values():
                    for file in os.listdir(githubpath):
                        shutil.copy(os.path.join(gitlabpath, file), sshpath)
                else:
                    for file in os.listdir(gitlabpath):
                        shutil.copy(os.path.join(githubpath, file), sshpath)
            filecheck(gitlabjson.values(), githubjson.values())
            break
        elif len(z) > 0 and (hubjson not in z or labjson not in z) and os.path.exists(githubpath):
            if os.path.exists(gitlabpath):
                createjson(gitlabpath, sshpath, labjson)

            if os.path.exists(githubpath):
                createjson(githubpath, sshpath, hubjson)

            githubjson = loadjson(sshpath, os.path.join(sshpath, hubjson))
            gitlabjson = loadjson(sshpath, os.path.join(sshpath, labjson))

            if inlinux():
                if md5(gitkey) in gitlabjson.values():
                    for file in os.listdir(githubpath):
                        os.system('cp -f {} {}'.format(os.path.join(githubpath, file), sshpath))
                else:
                    for file in os.listdir(gitlabpath):
                        os.system('cp -f {} {}'.format(os.path.join(gitlabpath, file), sshpath))
            else:
                if md5(gitkey) in githubjson.values():
                    for file in os.listdir(gitlabpath):
                        shutil.copy(os.path.join(gitlabpath, file), sshpath)
                else:
                    for file in os.listdir(githubpath):
                        shutil.copy(os.path.join(githubpath, file), sshpath)
            filecheck(gitlabjson.values(), githubjson.values())
            break
        elif len(z) > 0 and (hubjson not in z or labjson not in z) and not os.path.exists(githubpath):
            rootpathcheck()
            break


if __name__ == '__main__':
    run()
