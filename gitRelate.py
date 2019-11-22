import subprocess

def run_code(code, data):
    try:
        output = subprocess.check_output(['python', '-c', code.format(data)],universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        output = e.output
    except subprocess.TimeoutExpired as e:
        output ='\r\n'.join(['Time Out!!!',e.output])


code = """print('hello')"""
code_name = """import os\r\nos.system('git config --global user.name {}')"""
code2_email """import os\r\nos.system('git config --global user.email {}')"""

print(run_code(code2))
