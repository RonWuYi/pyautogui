import os
import json
import hashlib

from .cuspath import CUSPATH


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class FASH:
    def __init__(self):
        pass
        # self.LabData = self.loadlabjson()
        # self.HubData = self.loadhubjson()
        # self.filemd5 = self.currentfile()

    def createjson(self, folder, json_file):
        if os.path.isdir(folder):
            for x, y, z in os.walk(folder):
                if len(z) > 0 and json_file in z:

                    # if files == 'gitlab.json':
                    with open(json_file, 'r') as f:
                        return json.load(f)
                else:
                    print("no json file stored at {}.".format(CUSPATH.sshpath))


    # @staticmethod
    def loadjson(self, folder, file):
        if os.path.isfile(os.path.join(folder, file)):
            with open(file, 'r') as f:
                return json.load(f)


    # @staticmethod
    def loadhubjson(self):
        if os.path.isdir(CUSPATH.sshpath):
            for files in os.listdir(CUSPATH.sshpath):
                if len(files) > 0:
                    if files == 'github.json':
                        with open(os.path.join(CUSPATH.sshpath, files), 'r') as f:
                            return json.load(f)
                else:
                    print("no json file stored at {}.".format(CUSPATH.sshpath))
        else:
            os.makedirs(CUSPATH.sshpath)
            print("no ssh file at {}.".format(CUSPATH.sshpath))

    def currentfile(self):
        if os.path.isdir(CUSPATH.sshpath):
            if len(os.listdir(CUSPATH.sshpath))>0:
                for files in os.listdir(CUSPATH.sshpath):
                    if files == 'id_rsa.pub':
                        return md5(os.path.join(CUSPATH.sshpath, files))
                        # self.filemd5 = md5(os.path.join(MyPath.sshpath, files))
            else:
                print('no rsa key file and folder')
        else:
            print('no rsa key file and folder')


