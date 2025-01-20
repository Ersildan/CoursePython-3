def parse_ranges(ranges):
    split_comma_ranges = lambda s: (r.split('-') for r in s.split(','))
    generate_ranges = lambda bounds: (range(int(start), int(end) + 1) for start, end in bounds)
    return (j for i in generate_ranges(split_comma_ranges(ranges)) for j in i)


print(*parse_ranges('12-14')) # exmpl