list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = 0
prob = 0
for id, val in enumerate (list_numbers):
    if val >= max_:
        max_ = val
        max_id = id

list_numbers[max_id] = list_numbers[-1]
list_numbers[-1] = max_
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
