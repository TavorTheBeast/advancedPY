def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    primes = (x for x in range(n + 1, 2 * n) if is_prime(x))
    return next(primes)



print(first_prime_over(1000000))
