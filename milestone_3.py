"""
Ask for the user for a valid input continuously
"""

while True: # Create a continuous while loop
    guess = str(input('Enter single letter: '))

    # Check input is a single character and letter
    if len(guess) == 1 and guess.isalpha():
        # break out of loop
        break

    else:
        # print and go back to start
        print('Invalid letter. Please, enter a single alphabetical character.')