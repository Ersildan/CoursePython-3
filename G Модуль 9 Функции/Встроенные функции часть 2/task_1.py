def hash_as_key(d):
    res, res_ = dict(), dict()
    for el in d:
        res[hash(el)] = res.get(hash(el), []) + [el]
    for key, value in res.items():
        if len(value) > 1: res_[key] = value
        else: res_[key] = value[0]
    return res_