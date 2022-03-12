import random

def get_password():
    letters = [char for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    numbers = [char for char in "0123456789"]
    symbols = [char for char in "!@#$%^&*()_+-=[]|;:,./<>?"]

    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    password = []

    for i in range(nr_letters):
        password.append(random.choice(letters))

    for i in range(nr_numbers):
        password.append(random.choice(numbers))

    for i in range(nr_symbols):
        password.append(random.choice(symbols))

    random.shuffle(password)

    password = "".join(password)

    return password