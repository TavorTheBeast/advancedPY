numbers = iter(list(range(1, 101)))
next(numbers)  # Skip the first number
for i in numbers:
    next(numbers)  # Skip the second number
    print(i)
