import csv
import json
from collections import Counter

res = Counter()

for f in ("quarter1.csv", "quarter2.csv", "quarter3.csv", "quarter4.csv"):
    with open(f, encoding='UTF-8') as file:
        data = list(csv.reader(file, delimiter=','))
        del data[0]
        my_d = {d[0]: sum(map(int, d[1:])) for d in data}
    res += my_d

with open('prices.json', encoding="utf-8") as file_price:
    data = json.load(file_price)
    total = sum(data[i] * res[i] for i in res)
print(total)
