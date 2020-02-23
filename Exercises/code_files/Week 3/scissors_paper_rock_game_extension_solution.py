def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'

    return choice

def play_game():
    my_choice = input('Choose rock, scissors or paper: ')
    opponent_choice = random_choice()

    print('Your opponent chose {}'.format(opponent_choice))

    if my_choice == 'rock' and opponent_choice == 'scissors':
        print('You win!')

    elif my_choice == 'scissors' and opponent_choice == 'rock':
        print('I win!')

    elif my_choice == 'paper' and opponent_choice == 'scissors':
        print('You win!')

    elif my_choice == 'scissors' and opponent_choice == 'paper':
        print('I win!')

    elif my_choice == 'paper' and opponent_choice == 'rock':
        print('You win!')

    elif my_choice == 'rock' and opponent_choice == 'paper':
        print('I win!')

    else:
        print('We draw!')

    run_again = input('Would you like to play again?')

    if run_again == 'yes':
        play_game()

play_game()