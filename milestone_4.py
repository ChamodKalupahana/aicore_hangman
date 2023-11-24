# Import modules

import random

# Define Hangman class

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list

        #The number of lives the player has at the start of the game.
        self.num_lives = num_lives

        # Select random item from list
        self.word = random.choice(word_list)

        # A list of the letters of the word, with _ for each letter not yet guessed
        self.word_guessed = ['_' for item in self.word]

        # The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = len(set(self.word))

        # A list of the guesses that have been tried. Will be appended to as game plays
        self.list_of_guesses = []

    def check_guess(self, guess):
        # check guess letter is in word
        if guess in self.word:
            print('Good guess! {guess} is in the word.'.format(guess = guess))

            for letter_index in range(len(self.word)):
                if guess == self.word[letter_index]:
                    self.word_guessed[letter_index] = guess
            
            self.num_letters -= 1

        else:
            print('Sorry, {guess} is not in the word. Try again'.format(guess = guess))

            self.num_lives -= 1
            print('You have {num_lives} lives left.'.format(num_lives = self.num_lives))
    
    def ask_for_input(self):
        while True:
            guess = str(input('Enter single letter: '))
            guess = guess.lower()

            # Check input is a single character and letter
            if len(guess) != 1 or guess.isalpha() == False:
                # print and go back to start
                print('Invalid letter. Please, enter a single alphabetical character.')

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

# Define list of 5 favourite fruits
word_list = ['apple', 'grapes', 'banana', 'blueberries', 'strawberries']


test = Hangman(word_list)

test.ask_for_input()
