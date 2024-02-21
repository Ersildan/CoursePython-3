from zipfile import ZipFile
from datetime import datetime as dt

with ZipFile('workbook.zip') as zp:
    info = zp.infolist()
    d = dict()
    for f in info:
        if f.is_dir() is not True:
            values = (f.date_time, f.file_size, f.compress_size)
            if '/' in f.filename:
                k, v = f.filename.split('/')[1], values
                d[k] = v
            else:
                k, v = f.filename, values
                d[k] = v
    for name, information in sorted(d.items()):
        print(f'{name}')
        print(f'  Дата модификации файла: {dt(*information[0])}')
        print(f'  Объем исходного файла: {information[1]} байт(а)')
        print(f'  Объем сжатого файла: {information[2]} байт(а)')
        print()
