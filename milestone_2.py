# Import modules

import random

# Define list of 5 favourite fruits

word_list = ['apple', 'grapes', 'banana', 'blueberries', 'strawberries']

# Select random item from list

word = random.choice(word_list)

# Ask for user input

guess = str(input('Enter single letter: '))

# Check input is a single character

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')

else:
    print('Oops! That is not a valid input.')