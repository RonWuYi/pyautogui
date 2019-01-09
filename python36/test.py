import hashlib
import os
import json

from collections import OrderedDict


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# for x, y, z in os.walk('/home/hdc/.ssh'):
#     for i in z:
#         # print(os.path.join(x[0], y[0]))
#         # print(i + ' hash value is ' + md5(i))
#         print(i)
gitlabpath = '/home/hdc/.ssh/gitlab/'
githubpath = '/home/hdc/.ssh/github/'
sshpath = '/home/hdc/.ssh/'

githubmd5 = []
gitlabmd5 = []

# githubD = gitlabD = OrderedDict()
# gitlabD = OrderedDict()
githubD = {}
gitlabD = {}
for zz in os.listdir(gitlabpath):
    # print(zz)
    if 'git' not in zz:
        fmd5 = md5(os.path.join(gitlabpath, zz))
        # print(zz + ' hash value is '+ fmd5)

        gitlabmd5.append(fmd5)
        gitlabD[zz] = fmd5




for zz in os.listdir(githubpath):
    # print(zz)
    if 'git' not in zz:
        fmd5 = md5(os.path.join(githubpath, zz))
        # print(zz + ' hash value is '+md5(os.path.join(githubpath, zz)))

        githubmd5.append(fmd5)
        githubD[zz] = fmd5


print('---------------gitlab--------------------')
print(gitlabmd5)
print('---------------github--------------------')
print(githubmd5)


print('---------------json--------------------')
for key in gitlabD:
    print(key, gitlabD[key])

for key in githubD:
    print(key, githubD[key])
#
with open('gitlab.json', 'w') as f:
    json.dump(gitlabD, f)
#
with open('github.json', 'w') as f:
    json.dump(githubD, f)

