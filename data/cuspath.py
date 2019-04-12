# import os
# import zipfile
# import platform
#
# from pathlib import Path
# from .ftp import myftp, mydropbox, internet_on
#
#
#
#
#
#
#     def rootpathcheck(cls):
#         if not os.path.exists(cls().sshpath):
#             if internet_on():
#                 mydropbox()
#                 if os.path.isfile(os.path.join((str(Path.home())), 'ssh.zip')):
#                     zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
#                     zip_ref.extractall(path=cls().sshpath)
#                     zip_ref.close()
#                     os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
#                 else:
#                     print("get file from dropbox failed")
#             elif myftp(str(Path.home())):
#                 # myftp(str(Path.home()))
#                 zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
#                 zip_ref.extractall(path=cls().sshpath)
#                 zip_ref.close()
#                 os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
#             else:
#                 print("either cannot connect to Interent or cannot connect to ftp")
#         elif len(os.listdir(cls().sshpath)) == 0:
#             if internet_on():
#                 mydropbox()
#                 if os.path.isfile(os.path.join((str(Path.home())), 'ssh.zip')):
#                     zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
#                     zip_ref.extractall(path=cls().sshpath)
#                     zip_ref.close()
#                     os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
#                 else:
#                     print("get file from dropbox failed")
#             elif myftp(str(Path.home())):
#                 # myftp(str(Path.home()))
#                 zip_ref = zipfile.ZipFile(os.path.join(str(Path.home()), 'ssh.zip'), 'r')
#                 zip_ref.extractall(path=cls().sshpath)
#                 zip_ref.close()
#                 os.remove(os.path.join(str(Path.home()), 'ssh.zip'))
#             else:
#                 print("either cannot connect to Interent or cannot connect to ftp")
#         else:
#             print('id_rsa.pub file already exist')
pass
