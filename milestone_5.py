# Import modules

import random

# Define Hangman class

class Hangman():
    """
    The Hangman class represents a simple implementation of the classic Hangman game.
    Use ask_for_input() method to start the game once

    Attributes:
        - word_list (list): List of words for the Hangman game to randomly choose from.
        - num_lives (int, optional): Number of lives the player has at the start of the game. Defaults to 5.
        - word (str): The randomly chosen word from the word_list.
        - word_guessed (list): A list of the letters of the word, with '_' for each letter not yet guessed.
        - num_letters (int): The number of unique letters in the word that have not been guessed yet.
        - list_of_guesses (list): A list of the guesses that have been tried.
    """
    def __init__(self, word_list, num_lives = 5):
        """ Initialise the Hangman game

        Args:
            word_list (list): list of words for the Hangman game to randomly choose from for the hidden word
            num_lives (int, optional): Defaults to 5.
        """
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
        """ Check if the guessed letter is in the hidden word.

        Args:
            guess (str): single alphabetical letter to test if it's in the hidden word
        """
        # check guess letter is in word
        if guess in self.word:
            print('Good guess! {guess} is in the word.'.format(guess = guess))

            # update the word_guessed list for each occurrence of the guessed letter.
            for letter_index in range(len(self.word)):
                if guess == self.word[letter_index]:
                    self.word_guessed[letter_index] = guess
            
            # Decrement the number of unique letters in the word that have not been guessed yet.
            self.num_letters -= 1

        else:
            # Decrement the number of lives and inform the player.
            self.num_lives -= 1
            print('Sorry, {guess} is not in the word. Try again'.format(guess = guess))
            print('You have {num_lives} lives left.'.format(num_lives = self.num_lives))
    
    def ask_for_input(self):
        """Ask the player for a single letter as input.

        Prompts the player for input until a valid letter is provided.

        Args:
            None
        Returns:
            None
        """
        #while True: move while loop to play game function
        guess = str(input('Enter single letter: '))
        guess = guess.lower()

        # Check input is a single character and letter
        if len(guess) != 1 or guess.isalpha() == False:
            # print and go back to start
            print('Invalid letter. Please, enter a single alphabetical character.')

        # Check if the letter has already been guessed.
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")

        else:
            # Call the check_guess method with the player's guess.
            self.check_guess(guess)

            # Add the guess to the list of guesses.
            self.list_of_guesses.append(guess)


def play_game(word_list):
    # Define number of lives
    num_lives = 5

    # Create instance of Hangman class
    game = Hangman(word_list, num_lives)

    while True:
        # Check if user has run out of lives
        if game.num_lives == 0:
            print('You lost!')
            break
        
        # Continue playing if there are more letters to guess
        if game.num_letters > 0:
            game.ask_for_input()
        
        else:
            print('Congratulations. You won the game!')
            break


# Define list of 5 favourite fruits
word_list = ['apple', 'grapes', 'banana', 'blueberries', 'strawberries']

play_game(word_list)