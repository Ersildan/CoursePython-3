from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if by_values is False:
        [ordered_dict.move_to_end(k) for k in sorted(ordered_dict)]
    else:
        [ordered_dict.move_to_end(k) for k, v in sorted(ordered_dict.items(), key=lambda x: int(x[1]))]


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())
