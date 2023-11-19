from datetime import date

def get_min_max(l):
    if len(l) > 0:
        return (min(l), max(l),)
    else:
        return None
