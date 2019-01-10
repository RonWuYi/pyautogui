import subprocess

def gitconnectioncheck(whichgit):
    try:
        #out_bytes = subprocess.check_output(["ssh", "-T", "git@gitlab.emea.irdeto.com"], timeout=3)
        subprocess.check_output(["ssh", "-T", whichgit], timeout=3, stderr=subprocess.STDOUT)
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        out_bytes = e.output
        try:
            code = e.returncode
            print(out_bytes[0:10])
            print(code)
        except AttributeError as e:
            print(e)
        return False
