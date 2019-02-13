import os
import pathlib


target_file = os.path.join(pathlib.Path.cwd(), "DeviceData01.bin")


def get_cssn():
    if os.path.isfile(target_file):
        with open(target_file, 'rb') as f:
            byte = f.read()
            s = ""
            for i in range(4):
                y = format(byte[i], 'x')
                if len(y) == 1:
                    s += '0'+format(byte[i], 'x')
                else:
                    s += format(byte[i], 'x')
            return s
    else:
        print("no device bin file contains on current folder")

if __name__ == '__main__':
    get_cssn()
