import functools

def is_prime(number):
    return all(number % i != 0 for i in functools.reduce(lambda acc, val: acc + [val] if val * val <= number else acc, range(2, number), []))

print(is_prime(42))
print(is_prime(43))