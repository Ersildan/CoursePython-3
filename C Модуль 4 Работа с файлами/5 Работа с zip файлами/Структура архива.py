from zipfile import ZipFile


def foo(size):
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'


with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    for el in info:
        name = el.filename
        wt = el.file_size
        n_split = len(name[:-1].split('/')) - 1
        if el.is_dir():
            print(f"{'  ' * n_split}{name[:-1].split('/')[-1]}")
        else:
            print(f"{'  ' * n_split}{name.split('/')[-1]} {foo(wt)}")

'''Необходим зип файл для работы кода'''
