import os
import subprocess

try:
    os.system('ssh-add -D')
    subprocess.check_output(["ssh", "-T", whichgit], timeout=3, stderr=subprocess.STDOUT)
    return True
except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
    out_bytes = e.output
    try:
        code = e.returncode
        if out_bytes[0:2] == b'Hi' or out_bytes[0:7] == b'Welcome' and code == 1:
            return True
        else:
            return False
    except AttributeError as e:
        print(e)
        return False