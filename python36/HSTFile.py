import pathlib
#import os
# print(pathlib.Path.cwd())
import array

a = array.array('i', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#with open(os.path.join(pathlib.Path.cwd(), "testdata\\DeviceData.bin"), "rb") as f:
with open("C:\\Work\\Github\\pyautogui\\testdata\\DeviceData.bin", "rb") as f:
    f.readinto(a)


print(a)
    # byte =f.read(1)
    # while byte:
    #     byte  =f.read(8)
    #     print(byte)
        # text =byte.decode('utf-8')
        # print(text)