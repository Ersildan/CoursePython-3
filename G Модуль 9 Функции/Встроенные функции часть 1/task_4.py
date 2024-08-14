def non_negative_even(l):
    return all([i >= 0 and i % 2 == 0 for i in l])
