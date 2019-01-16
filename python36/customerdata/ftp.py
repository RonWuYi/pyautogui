import os

from ftplib import FTP


def myftp(path):
    ftp = FTP('172.16.66.149')
    ftp.login('anonymous', '123')

    files = ftp.nlst()

    for file in files:
        if file == 'ssh.zip':
            ftp.retrbinary("RETR " + file, open(os.path.join(path, file), 'wb').write)
    ftp.close()
