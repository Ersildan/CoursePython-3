from datetime import date

def is_correct(d, m, y):
    try:
        date(y, m, d)
        return True
    except:
        return False
