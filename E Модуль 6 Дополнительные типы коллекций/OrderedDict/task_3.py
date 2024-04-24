from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if by_values is False:  # key sorted

        ordered_dict = sorted(ordered_dict, key=lambda x: x[0])
    else:
        ordered_dict = sorted(ordered_dict, key=lambda x: x[1])
    pass

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)
print()
print(sorted(data.keys()))
print(sorted(data.values()))
