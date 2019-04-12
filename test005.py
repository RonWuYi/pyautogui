import os


from pathlib import Path


gitlabpath = os.path.join(Path.home(), '.ssh', 'gitlab')
githubpath = os.path.join(Path.home(), '.ssh', 'github')
sshpath = os.path.join(Path.home(), '.ssh')

print(sshpath)

pass