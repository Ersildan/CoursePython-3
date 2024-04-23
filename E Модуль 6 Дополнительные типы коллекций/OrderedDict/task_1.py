from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
                    'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
                    'SeatsCount': '10'})

print(OrderedDict(reversed(data.items())))

data2 = OrderedDict(key1='value1', key2='value2', key3='value3')

print(OrderedDict(reversed(data2.items())))
