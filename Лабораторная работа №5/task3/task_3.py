from random import sample


def get_unique_list_numbers(a, b, c) -> list[int]:
    return [i for i in sample(range(b, c+1), a)]


list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
