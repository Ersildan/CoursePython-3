import copy

def get_min_max(iterable):
    try:
        iterable_copy = copy.copy(iterable)
        return min(iterable), max(iterable_copy)
    except:
        None
