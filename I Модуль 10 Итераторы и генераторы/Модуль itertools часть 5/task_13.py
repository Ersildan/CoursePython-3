from itertools import product

def password_gen():
    for a,b,c in product(range(10), repeat=3):
        yield f"{a}{b}{c}"


passwords = password_gen()
print(next(passwords))
print(next(passwords))
print(next(passwords))
print(next(passwords))
print(next(passwords))
print(next(passwords))
