import os

my_path = "C:\\Users\\ron.wu\\Downloads\\ffmpeg64bit411"

my_list = []

for x, y, z in os.walk(my_path):
    if len(z) > 0:
        for i in z:
            if i[-3:] == "lib":
                print(i)
                if i not in my_list:
                    my_list.append(i)


print("#######################################")
for i in my_list:
    print(i)

