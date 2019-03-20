import os
from pathlib import Path
# from ftplib import FTP
#
#
# def myftp(path):
#     try:
#         ftp = FTP('172.16.66.149', 5)
#     except (ConnectionResetError, ConnectionRefusedError, ConnectionError, ConnectionAbortedError) as e:
#         print(e)
#         return
#     ftp.login('anonymous', '123')
#     files = ftp.nlst()
#     for file in files:
#         if file == 'ssh.zip':
#             ftp.retrbinary("RETR " + file, open(os.path.join(path, file), 'wb').write)
#     ftp.close()


# def mydropbox(path):
os.chdir(Path.home())
os.system("dir")