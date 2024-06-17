def is_good_password(s):
    return all([
                any(i.isdigit() for i in s),
                len(s) >= 9, not s.isupper() and not s.islower(),
                any(i.isalpha() for i in s)
                ])
