from zipfile import ZipFile
import json
import os.path


def foo():
    pass


with ZipFile('test.zip') as zip_file:
    for el in zip_file.infolist():
        if not el.is_dir():
            print(el.filename.split("/")[-1])
        else:
            print(f'{el.filename}')


