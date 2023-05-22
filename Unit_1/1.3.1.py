import functools

def intersection(list_1, list_2):
    return [x for x in functools.reduce(lambda acc, val: acc + [val] if val in list_2 and val not in acc else acc, list_1, [])]


print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))