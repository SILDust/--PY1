from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n=8) -> str:
    all_list = ascii_lowercase + ascii_uppercase + digits
    password_list = sample(all_list, n)
    return "".join(password_list)


print(get_random_password(8))
