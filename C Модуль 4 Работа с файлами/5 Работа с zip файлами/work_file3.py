from zipfile import ZipFile


def extract_this(zip_name='', *args):
    with ZipFile(zip_name) as fz:
        if len(args) != 0:
            for f in args:
                fz.extract(f)
        else:
            fz.extractall()


extract_this('workbook.zip', 'python.pdf', 'test.py')