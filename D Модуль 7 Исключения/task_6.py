def add_to_list_in_dict(data, key, element):
    return data.setdefault(key, []).append(element)
