import os
import shutil

# from data.util import *
# from data.const import *
from data.util import sshpath, inlinux, md5, filecheck, check_wrapper, loadjson, create_json, rootpathcheck
from data.const import hubjson, labjson, githubpath, gitlabpath, gitkey

def run() -> None:
    if os.path.exists(sshpath) and len(os.listdir(sshpath)):
        for _, _, z in os.walk(sshpath):
            if len(z) > 0 and hubjson in z and labjson in z:
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
                check_wrapper()
                break
            elif len(z) > 0 and (hubjson not in z or labjson not in z):
                if os.path.exists(gitlabpath):
                    create_json(gitlabpath, sshpath, labjson)

                if os.path.exists(githubpath):
                    create_json(githubpath, sshpath, hubjson)

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
                check_wrapper()
                break
    elif os.path.exists(sshpath) and not len(os.listdir(sshpath)):
        # folder_file = False
        rootpathcheck()
    else:
        rootpathcheck()


if __name__ == '__main__':
    run()
