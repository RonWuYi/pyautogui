# import os
# import json
# import hashlib
#
# from .const import *
#
#
# def md5(fname):
#     hash_md5 = hashlib.md5()
#     with open(fname, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()
#
#
# class FASH:
#     def createjson(self, folder, json_file):
#         if os.path.isdir(folder):
#             for x, y, z in os.walk(folder):
#                 if len(z) > 0 and json_file in z:
#
#                     # if files == 'gitlab.json':
#                     with open(json_file, 'r') as f:
#                         return json.load(f)
#                 else:
#                     print("no json file stored at {}.".format(sshpath))
#
#     def loadjson(self, folder, file):
#         if os.path.isfile(os.path.join(folder, file)):
#             with open(file, 'r') as f:
#                 return json.load(f)
#
#     def loadhubjson(self):
#         if os.path.isdir(sshpath):
#             for files in os.listdir(sshpath):
#                 if len(files) > 0:
#                     if files == 'github.json':
#                         with open(os.path.join(sshpath, files), 'r') as f:
#                             return json.load(f)
#                 else:
#                     print("no json file stored at {}.".format(sshpath))
#         else:
#             os.makedirs(sshpath)
#             print("no ssh file at {}.".format(sshpath))
#
#     def currentfile(self):
#         if os.path.isdir(sshpath):
#             if len(os.listdir(sshpath))>0:
#                 for files in os.listdir(sshpath):
#                     if files == 'id_rsa.pub':
#                         return md5(os.path.join(sshpath, files))
#
#             else:
#                 print('no rsa key file and folder')
#         else:
#             print('no rsa key file and folder')
#
#

pass
