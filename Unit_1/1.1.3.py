import functools

def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, functools.reduce(lambda acc, x: acc + [x + 1], range(number), [])))

print(four_dividers(9))
print(four_dividers(3))