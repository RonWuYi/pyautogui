import pathlib
#import os
# print(pathlib.Path.cwd())
import array
import struct
a = array.array('i', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#with open(os.path.join(pathlib.Path.cwd(), "testdata\\DeviceData.bin"), "rb") as f:
with open("C:\\Work\\Github\\pyautogui\\testdata\\DeviceData.bin", "rb") as f:
    # f.readinto(a)
    # fileconten = f.read()
    # print(struct.unpack("iiiii", fileconten[:20]))

#
# print(a)
    byte =f.read(1)
    while byte:
        byte  =f.read(1)
        print(byte)
#         text =byte.decode('ascii')
#         print(text)