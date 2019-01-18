import os
import json
import hashlib

from .cuspath import CUSPATH

MyPath = CUSPATH()

    # @staticmethod
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class filehash:
    def __init__(self, labdata = {}, hubdata = {}, filemd5 = 0):
        self.LabData = labdata
        self.HubData = hubdata
        self.filemd5 = filemd5
        self.loadjson()
        self.currentfile()

    # @staticmethod
    def loadjson(self):
        for files in os.listdir(MyPath.sshpath):
            if len(files) > 0:
                if files == 'gitlab.json':
                    with open(os.path.join(MyPath.sshpath, files), 'r') as f:
                        self.LabData = json.load(f)
                    break
            else:
                print("no json file stored at {}.".format(MyPath.sshpath))

        for files in os.listdir(MyPath.sshpath):
            if len(files) > 0:
                if files == 'github.json':
                    with open(os.path.join(MyPath.sshpath, files), 'r') as f:
                        self.HubData = json.load(f)
                    break
            else:
                print("no json file stored at {}.".format(MyPath.sshpath))

    def currentfile(self):
        for files in os.listdir(MyPath.sshpath):
            if files == 'id_rsa.pub':
                self.filemd5 = md5(os.path.join(MyPath.sshpath, files))


