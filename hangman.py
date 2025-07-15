import random
import string
from words import words  

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()  

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters remaining to guess
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()  # Letters user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left. Guessed letters: {' '.join(sorted(guessed_letters))}")

        # Show current progress
        word_display = [letter if letter in guessed_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_display))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("That letter is not in the word.")
        elif user_letter in guessed_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please enter a valid letter.")

    if lives == 0:
        print(f"\nYou lost. The word was {word}.")
    else:
        print(f"\nYou guessed the word {word}! You win!")

hangman()
