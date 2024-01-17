import random


def random_number_generator():
    number = random.randint(1,6)
    return number





number = random_number_generator()
print("Todays lucky number is: ", number)