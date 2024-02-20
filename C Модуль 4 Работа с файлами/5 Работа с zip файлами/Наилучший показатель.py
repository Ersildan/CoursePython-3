from zipfile import ZipFile

with ZipFile('workbook.zip') as zp:
    info = zp.infolist()
    lst = [f for f in info if f.is_dir() is False]
    file = min(lst, key=lambda x: (x.compress_size/x.file_size))
    print(file.filename.split('/')[1])
