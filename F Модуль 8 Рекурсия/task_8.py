def linear(my_list):
    l = []
    for el in my_list:
        if (isinstance(el, list)):
            l.extend(linear(el))
        else:
            l.append(el)
    return l

