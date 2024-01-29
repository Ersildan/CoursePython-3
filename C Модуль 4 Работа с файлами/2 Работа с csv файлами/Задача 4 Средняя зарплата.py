import csv

with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    my_dict_1 = dict()
    my_dict_2 = dict()
    my_dict_3 = dict()

    expensive = sorted(rows, key=lambda x: (int(x['salary']), x['company_name']))

    for d in expensive:
        my_dict_1[d['company_name']] = my_dict_1.get(d['company_name'], 0) + 1
        my_dict_2[d['company_name']] = my_dict_2.get(d['company_name'], 0) + int(d['salary'])
    for k, v in my_dict_1.items():
        my_dict_3[k] = my_dict_2[k]/v
    print(*[i[0]for i in sorted(my_dict_3.items(), key=lambda x: (x[1], x[0]))], sep='\n')
