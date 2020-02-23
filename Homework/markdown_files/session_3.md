<p align="center">
  <img src="logo.png">
</p>

# CodeFirstGirls Beginners Python

# Homework: Session 3

Topics in this session:

1. Comparison Operators
1. Logical Operators
1. If Statements


Additional resources:

- Comparisons <https://realpython.com/python-operators-expressions/>

- if statements <https://realpython.com/python-conditional-statements/>


# Task 1

Create a program that tells you whether or not you need an umbrella when you leave the house.

The program should:

1. Ask you if it is raining using `input()`

1. If the input is 'y', it should output 'Take an umbrella'

1. If the input is 'n', it should output 'You don't need an umbrella'

# Task 2

I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've written a program to check that I can afford the cost, but something doesn't seem right. 

Have a look at my program and work out what I've done wrong

```python
my_money = input('How much money do you have? ')
boat cost = 20 + 5

if my_money < boat_cost:
	print('You can afford the boat hire')
else:
	print('You cannot afford the board hire')
```

# Task 3
Complete the following for each of your answers to exercise 3.6 - 3.8 in the class

### Task 3.1
Ensure the program still runs correctly if the user gives captialised or lowercase text as inputs.

### Task 3.2 
Check that the user inputs are valid before running the game. 

For example, in roulette game, the colours can only be 'red' or 'black'.
If the user inputs another colour, ask the user to input again, 
choosing between the valid colours.
Example: 

``` python 
chosen_colour = input('Input a colour, red or black:')
```
The program should then check if the colour is red or black. 
If the user inputs another colour, such as green, the program should ask them to 
input a new colour:

``` python
chosen_colour = input('Only red or black valid colours. 
                        Please enter valid colour:')
```

### Task 3.3
Ask the user if they want to play again at the end of the program. If the user inputs 'yes', run the game again.