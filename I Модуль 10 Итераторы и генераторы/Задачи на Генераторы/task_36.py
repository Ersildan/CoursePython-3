def nonempty_lines(file):
    with open(file, encoding='UTF-8') as f:
        return (
                line.strip() if len(line) <= 25 else '...'
                for line in f.readlines()
                if len(line.strip()) != 0
               )
    pass
