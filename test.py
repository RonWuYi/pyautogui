import os
import json


path = "C:\\sandbox\\.ssh"

for x, y, z in os.walk(path):
    if len(z) > 0:
        for i in z:
            print(i)
