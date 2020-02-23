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

bet = input('How much do you want to bet? ')
chosen_colour = input('Pick a colour (red or black): ')
chosen_number = input('Pick a number (between 1 and 100): ')

print('The wining colour is: ' + str(random_number))
print('The wining number is: ' + str(random_colour))

if chosen_colour == random_colour and chosen_number == random_number:
    win_value = float(bet)*100
    print('You win: ' + str(win_value))

elif chosen_colour == random_colour:
    print('You win: ' + bet)

elif chosen_number == random_number:
    win_value = float(bet)*2
    print('You win: ' + str(win_value))

else:
    print('You win: 0')

