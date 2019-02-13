import os
import json
import hashlib

from .cuspath import CUSPATH

MyPath = CUSPATH()


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class filehash:
    def __init__(self, labdata={}, hubdata={}, filemd5=0):
        self.LabData = labdata
        self.HubData = hubdata
        self.filemd5 = filemd5
        self.loadjson()
        self.currentfile()

    # @staticmethod
    def loadjson(self):
        if os.path.isdir(MyPath.sshpath):
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
        else:
            os.makedirs(MyPath.sshpath)
            print("no ssh file at {}.".format(MyPath.sshpath))

    def currentfile(self):
        if os.path.isdir(MyPath.sshpath):
            if len(os.listdir(MyPath.sshpath))>0:
                for files in os.listdir(MyPath.sshpath):
                    if files == 'id_rsa.pub':
                        self.filemd5 = md5(os.path.join(MyPath.sshpath, files))
            else:
                return False
        else:
            print('no rsa key file and folder')


