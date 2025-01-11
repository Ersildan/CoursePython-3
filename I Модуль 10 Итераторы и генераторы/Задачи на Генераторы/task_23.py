def flatten(nested_list):
    new_lst = str(nested_list).replace('[', '').replace(']','')
    yield from new_lst




