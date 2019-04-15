import os
import subprocess

from data.const import *
from data.util import *


# r = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
# print(r.stdout)


r = subprocess.run(["ssh", "-T", "git@github.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("stdout = ", r.stdout)

print(len(r.stdout))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("stderr = ", r.stderr)
print(len(r.stderr))
