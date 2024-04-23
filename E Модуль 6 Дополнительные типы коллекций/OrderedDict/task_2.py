from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
                    'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
                    'SeatsCount': '10'
                    })
new_data = OrderedDict()
for rule in (i % 2 == 1 for i in range(len(data))):
    name, grade = data.popitem(last=rule)
    new_data[name] = grade
print(new_data)
