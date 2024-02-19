from zipfile import ZipFile

with ZipFile('workbook.zip') as zp:
    lst = sum([i.file_size for i in zp.infolist()])
    lst_ = sum([i.compress_size for i in zp.infolist()])

    print(f"Объем исходных файлов: {lst} байт(а)")
    print(f"Объем сжатых файлов: {lst_} байт(а)")
