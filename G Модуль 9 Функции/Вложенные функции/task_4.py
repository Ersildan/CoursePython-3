from datetime import date

def date_formatter(country_code):
    d = {
        'ru': '%d.%m.%Y',
        'us':  '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr':  '%d.%m.%Y',
        'pt': '%d-%m-%Y'
        }
    return lambda date: date.strftime(d[country_code])

