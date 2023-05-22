def parse_ranges(ranges_string):
    ranges = ranges_string.split(',')
    number_generator = (parse_range(range_str) for range_str in ranges)
    return (number for generator in number_generator for number in generator)

def parse_range(range_str):
    start, end = range_str.split('-')
    return range(int(start), int(end) + 1)


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))