import zipfile, os, shutil, tempfile
path = input('Path to the archive:')
folder = input('Folder name:')
path2 = input('Path to the folder')
os.makedirs(path2 + '\\' + folder)
with tempfile.TemporaryDirectory() as path3:
    one_zip = zipfile.ZipFile(path)
    one_zip.extractall(path3)
    for root, dirs, files in os.walk(path3):
        for file in files:
            shutil.copy(root + '\\' + file, path2 + '\\' + folder)
