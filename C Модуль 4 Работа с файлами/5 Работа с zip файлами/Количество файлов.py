from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    zip_file.printdir()

"need open file"