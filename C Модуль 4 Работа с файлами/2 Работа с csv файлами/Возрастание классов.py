import csv

with open('student_counts.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=','))
    file.seek(0)
    text = file.readline().strip().split(',')
    lst_keys = ['year'] + sorted(text[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))

    lst = []
    for d in data:
        temp_lst = []
        for k in lst_keys:
            temp_lst.append(d[k])
        lst.append(temp_lst)

    with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        writer.writerows([lst_keys] + lst)
