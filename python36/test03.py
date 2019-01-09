import os
import subprocess
# if 'Welcome to GitLab' in os.popen('ssh -T git@gitlab.emea.irdeto.com').read():
#     print('change to git lab success')
# else:
#     print('failed change to git lab')




# proc = os.popen("ssh -T git@github.com")
# (out, err) = proc.communicate()
proc1 = subprocess.check_output(['ssh', '-T', 'git@github.com'], shell=False)
# if 'Hi RonWuYi' in os.popen('ssh -T git@github.com').read():
#     print('change to git hub success')
# else:
#     print('failed change to git hub')
print(proc)
