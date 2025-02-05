def txt_to_dict():
    """def txt_to_dict():
        with open('planets.txt', encoding="UTF-8") as file:
            yield from (d for block in file.read().split("\n\n") if
                        (d := dict(line.split(" = ") for line in block.splitlines())))"""

    with open('planets.txt', encoding="UTF-8") as file:
        lst = file.read().split('\n')
        d = dict()

        for i in lst:
            if i != '':
                k, v = i.split(' = ')
                d[k] = v
            else:
                yield d
                d = dict()


planets = txt_to_dict()

print(next(planets))
print(next(planets))