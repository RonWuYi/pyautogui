import os
import json
import hashlib

from pathlib import Path

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

my_dict = {}
for x, y, z in os.walk(Path.cwd()):
    if len(z) > 0:
        for i in z:
            my_dict[i] = md5(os.path.join(x, i))

with open(os.path.join(Path.cwd(), 'files.json'), 'w') as f:
    json.dump(my_dict, f)
