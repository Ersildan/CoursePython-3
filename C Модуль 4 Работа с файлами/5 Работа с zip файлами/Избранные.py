from zipfile import ZipFile
from datetime import datetime as dt

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

    lst = []

    for f in info:
        y, m, d, H, M, S = f.date_time
        if dt(y, m, d, H, M, S) >= dt(2021, 11, 30, 14, 22, 00):
            lst.append(f.filename.split('/')[1] if "/" in f.filename else f.filename)

    lst = list(filter(lambda x: x != '', lst))
    print(*sorted(lst), sep='\n')
