from datetime import datetime as de

def fill_up_missing_dates(dates):
    pn = "%d.%m.%Y"
    lst = dates.copy()
    lst = [de.strptime(i, pn).toordinal() for i in lst]
    mn, mx = min(lst), max(lst)
    l = [de.strftime(de.fromordinal(i), pn) for i in range(mn, mx + 1)]
    return l
  
