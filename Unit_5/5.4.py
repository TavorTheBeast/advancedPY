class IDIterator:
    def __init__(self, id_number):
        self.id_ = id_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.id_ >= 999999999:
            raise StopIteration
        self.id_ += 1
        while not check_id_valid(self.id_):
            self.id_ += 1
        return self.id_


def check_id_valid(id_number):
    digits = [int(digit) for digit in str(id_number)]
    multiplied_digits = [digit * (2 if i % 2 == 0 else 1) for i, digit in enumerate(digits)]
    summed_digits = [digit if digit < 10 else digit // 10 + digit % 10 for digit in multiplied_digits]
    total_sum = sum(summed_digits)
    return total_sum % 10 == 0


def id_generator(id_number):
    while id_number < 999999999:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number


def main():
    id_number = int(input("Enter ID: "))
    iterator_or_generator = input("Generator or Iterator? (gen/it)? ")

    if iterator_or_generator == "it":
        iterator = IDIterator(id_number)
        id_numbers = [next(iterator) for _ in range(10)]
    elif iterator_or_generator == "gen":
        generator = id_generator(id_number)
        id_numbers = [next(generator) for _ in range(10)]

    for id_num in id_numbers:
        print(id_num)


if __name__ == "__main__":
    main()
