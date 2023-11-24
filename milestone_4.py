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

# Define list of 5 favourite fruits
word_list = ['apple', 'grapes', 'banana', 'blueberries', 'strawberries']


test = Hangman(word_list)
print(test.word)
print(test.num_letters)
