"""
Napisz skrypt zliczający ilość plików w katalogu /dev, skorzystaj ze standardowej biblioteki - os
"""

import os

def sprawdz_zawartosc():
    dev_path = '/dev/'
    os.chdir(dev_path)

    files_count = len(os.listdir())

    print('Ilość plików w folderze \'{path}\' : {count}'.format(path=dev_path, count=files_count))

if __name__ == "__main__":
   sprawdz_zawartosc()