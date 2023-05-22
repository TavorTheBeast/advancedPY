import functools

def sum_of_digits(number):
    return functools.reduce(lambda x, y: x + y, map(int, str(number)))


print(sum_of_digits(104))