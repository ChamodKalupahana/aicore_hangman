"""
Ask for the user for a valid input continuously for hangman
"""

# Import modules
import random

# Define functions for while loop
def check_guess(guess):
    # check guess letter is in word
    if guess in word:
        print('Good guess! {guess} is in the word.'.format(guess = guess))

    else:
        print('Sorry, {guess} is not in the word. Try again'.format(guess = guess))


def ask_for_input():
    guess = str(input('Enter single letter: '))
    guess = guess.lower()

    # Check input is a single character and letter
    if len(guess) == 1 and guess.isalpha():
        check_guess(guess)

    else:
        # print and go back to start
        print('Invalid letter. Please, enter a single alphabetical character.')


# Define list of 5 favourite fruits
word_list = ['apple', 'grapes', 'banana', 'blueberries', 'strawberries']

# Select random item from list
word = random.choice(word_list)


while True: # Create a continuous while loop
    ask_for_input()
        