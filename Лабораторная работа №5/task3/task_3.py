from random import sample


ef get_unique_list_numbers(quantity, low_threshold, upper_threshold) -> list[int]:
    return [i for i in sample(range(low_threshold, upper_threshold+1), quantity)]


list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
