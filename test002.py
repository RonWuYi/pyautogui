import os
path = "C:\\Users\\ron.wu\\Downloads\\ffmpeg411sdl2209\\ffmpeg411andsdl220932bit\\lib"

for x, y, z in os.walk(path):
    if len(z) > 0:
        for i in z:
            if i[-3:] == "lib":
                print(i)