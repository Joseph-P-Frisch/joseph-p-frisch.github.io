# hangman.py
# Name: Joseph P. Frisch
# Collaborators:
# Time spent: {~12 hours}

# Hangman Game
# -----------------------------------
# Helper code
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    # def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    my_word = ""

    for letter in secret_word:
        if letter in letters_guessed:
            my_word += letter
        else:
            my_word += " _ "
    return my_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    letters_guessed.sort()

    remaining_letters = ""

    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            remaining_letters += letter

    #remaining_letters.sort()

    return remaining_letters


def calculate_score(secret_word, guesses_remaining):
    unique_letters = []

    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)

    score = guesses_remaining * len(unique_letters)
    return score

"""
def hangman(secret_word):
    
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    
    letters_guessed = []
    letters_remaining = []  # assigns a list
    for letter in string.ascii_lowercase:  # iterates through the list to break it up and assign an index position to each value
        letters_remaining.append(letter)
    vowels = ["a", "e", "i", "o", "u"]
    guesses_remaining = 6
    warnings_remaining = 3

    while guesses_remaining > 0:

        print("--------------------------------")
        print(f"{guesses_remaining} guesses remain\n{warnings_remaining} warnings remain")
        print(f"available letters: ", get_available_letters(letters_guessed))
        print(get_guessed_word(secret_word, letters_guessed))
        guess = input("\ninput a letter ").lower()

        if guess in letters_remaining:
            letters_guessed.append(guess)
            letters_remaining.remove(guess)
            if guess in secret_word:
                print(f"{guess} is in secret_word")
                if is_word_guessed(secret_word, letters_guessed) == True:
                    break
            if guess not in secret_word:
                print(f"{guess} is not in secret_word")
                if guess in vowels:
                    guesses_remaining -= 2
                    continue
                else:
                    guesses_remaining -= 1
                    continue
        else:
            if guess in letters_guessed:
                print(f"{guess} already guessed")
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    continue
                if warnings_remaining == 0:
                    if guess in vowels:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    continue
            if guess not in string.ascii_letters:
                print(f"{guess} is not an allowed character")
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    continue
                if warnings_remaining == 0:
                    if guess in vowels:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    continue
                continue

    print("--------------------------------")

    if guesses_remaining > 0:
        print(f"You won! Your score is: {calculate_score(secret_word, guesses_remaining)}\n")
        print(f"The secret_word is {secret_word}. Play again by running code")
    else:
        print(f"Good luck next time.\n\nThe secret_word is {secret_word}. Play again by running code")
"""

# -----------------------------------

def match_with_gaps(my_word, other_word, letters_guessed):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    other_word = other_word.replace(" ", "")
    my_word = my_word.replace(" ", "")

    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] != other_word[i] and my_word[i] != "_":
                return False
            if my_word[i] == "_" and other_word[i] in letters_guessed:
                return False
        return True
    return False


def show_possible_matches(my_word, letters_guessed):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    """
    possible_words = []

    for word in wordlist:
        if match_with_gaps(my_word, word, letters_guessed):
            possible_words.append(word)

    if len(possible_words) <= 0:
        print("No possible matches found.")
    else:
        print("--------------------------------\n")
        print(f"possible words:\t{possible_words}")


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    letters_guessed = []
    letters_remaining = []  # assigns a list
    for letter in string.ascii_lowercase:  # iterates through the list to break it up and assign an index position to each value
        letters_remaining.append(letter)
    vowels = ["a", "e", "i", "o", "u"]
    guesses_remaining = 6
    warnings_remaining = 3

    while guesses_remaining > 0:

        print("\n--------------------------------")
        print(f"{guesses_remaining} guesses remain\t{warnings_remaining} warnings remain\t", end="")
        print(f"available letters: ", get_available_letters(letters_guessed))
        my_word = get_guessed_word(secret_word, letters_guessed)
        print(my_word)

        guess = input("input a letter\t").lower()
        while len(guess) != 1:
            guess = input(
                "input only one character: a letter. Other single characters will count as failed guesses\t").lower()

        if guess == "*":
            show_possible_matches(my_word, letters_guessed)
            if warnings_remaining > 0:
                warnings_remaining -= 1
            continue
        if guess in letters_remaining:
            letters_guessed.append(guess)
            letters_remaining.remove(guess)
            if guess in secret_word:
                print(f"{guess} is in secret_word")
                if is_word_guessed(secret_word, letters_guessed):
                    break
            if guess not in secret_word:
                print(f"{guess} is not in secret_word")
                if guess in vowels:
                    guesses_remaining -= 2
                    continue
                else:
                    guesses_remaining -= 1
                    continue
        else:
            if guess in letters_guessed:
                print(f"{guess} already guessed")
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    continue
                if warnings_remaining == 0:
                    if guess in vowels:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    continue
            if guess not in string.ascii_lowercase:
                print(f"{guess} is not an allowed character")
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    continue
                if warnings_remaining == 0:
                    if guess in vowels:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    continue
                continue

    print("--------------------------------")

    if guesses_remaining > 0:
        print(f"\nYou won! Your score is: {calculate_score(secret_word, guesses_remaining)}\n")
        print(f"The secret_word is {secret_word}. Play again by running code")
    else:
        print(f"Good luck next time.\n\nThe secret_word is {secret_word}. Play again by running code")


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)