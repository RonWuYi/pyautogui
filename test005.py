import os
from data.const import *
from data.util import *
# import subprocess
#
# from pathlib import Path
#
#
# gitlabpath = os.path.join(Path.home(), '.ssh', 'gitlab')
# githubpath = os.path.join(Path.home(), '.ssh', 'github')
# sshpath = os.path.join(Path.home(), '.ssh')
#
# os.system('cat ~/.ssh/gitlab.json')

#
# from subprocess import Popen, PIPE, STDOUT
#
# p = Popen(['sudo', 'i'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
# print(PIPE)
# grep_stdout = p.communicate(input=b'a\n', timeout=3)[0]
# print(grep_stdout.decode())

# proc = subprocess.Popen('sudo -i', stdin=PIPE).communicate('a')
# subpr('sudo cat {}'.format(os.path.join(githubpath, )), pip=)

# from subprocess import call
#
# pwd='a'
# cmd='chmod 777 ~/.ssh'
#
# call('sudo -i | echo {}'.format(pwd), shell=True, timeout=5)

print(md5(gitkey))

githubjson = loadjson(sshpath, os.path.join(sshpath, hubjson))
# githubjson

print(type(githubjson.values()))
# for i in githubpath:
#     print(type(i))