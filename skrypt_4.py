import os

dev_path = '/dev/'
os.chdir(dev_path)

files_count = len(os.listdir())

print('Ilość plików w folderze \'{path}\' : {count}'.format(path=dev_path, count=files_count))
