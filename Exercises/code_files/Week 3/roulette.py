import random

def colour():
    random_number = random.randint(1, 2)

    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'

    return colour

random_number = random.randint(1, 100)
random_colour = colour()