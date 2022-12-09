import random
import string


def get_random_password(n) -> str:
    all_list = [letter for letter in (string.ascii_lowercase + string.ascii_uppercase)] + \
               [str(digit) for digit in range(10)]
    password_list = random.sample(all_list, n)
    return "".join(password_list)


print(get_random_password(8))
