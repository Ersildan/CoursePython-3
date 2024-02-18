from zipfile import ZipFile

with ZipFile('workbook.zip') as zp:
    print(len([file for file in zp.infolist() if not file.is_dir()]))
