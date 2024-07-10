def recursive_sum(nested_lists):
    global total
    if len(nested_lists) == 0:
        return 0
    else:
        for i in nested_lists:
            if isinstance(i, int):
                total += i
            else:
                recursive_sum(i)


total = 0
