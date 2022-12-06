def get_random_password(n) -> str:
    import random
    all_list = [chr(random.randint(ord('a'), ord('z'))) for i in range(int(n))] +\
               [chr(random.randint(ord('A'), ord('Z'))) for i in range(int(n))] +\
               [random.randint(0, 9) for i in range(int(n))]
    password_list = random.sample(all_list, int(n))
    return "".join(map(str, password_list))

print(get_random_password(8))
