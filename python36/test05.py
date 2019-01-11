import os
import zipfile


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in file:
            ziph.write(os.path.join(root, file))


if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python2.zip', 'w', zipfile.ZIP_DEFLATED).extractall(pwd='Python')
    zipdir('tmp', zipf)
    # zipf.close()
