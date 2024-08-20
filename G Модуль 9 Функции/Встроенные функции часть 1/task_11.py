l1, l2, l3, l4 = [], [], [], []

for i in sorted(input()):
    if i.isdigit() and int(i) % 2 == 0:
        l4.append(i)
    elif i.isdigit() and int(i) % 2 == 1:
        l3.append(i)
    elif i == i.upper():
        l2.append(i)
    elif i == i.lower():
        l1.append(i)

print("".join(l1 + l2 + l3 + l4))