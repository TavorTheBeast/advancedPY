import functools

def double_letter(my_str):
    return functools.reduce(lambda acc, char: acc + char * 2, my_str, '')


print(double_letter("python"))
print(double_letter("we are the champions!"))