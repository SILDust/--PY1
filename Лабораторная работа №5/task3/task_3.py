def get_unique_list_numbers(a) -> list[int]:
    from random import randint
    return [randint(-10, 10) for _ in range(a)]


list_unique_numbers = get_unique_list_numbers(15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
