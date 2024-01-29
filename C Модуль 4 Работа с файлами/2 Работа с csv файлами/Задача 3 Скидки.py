with open('sales.csv', encoding='utf-8') as file:
    data = file.read()
    for line in data.splitlines()[1:]:
        name, old_price, new_price = line.split(';')
        if int(new_price) < int(old_price):
            print(name)
