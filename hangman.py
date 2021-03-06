# Hangman game
## This is just the project for MIT "Introduction to Computation and Programming with Python Course"#
# Let's add a new feature.#

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all([i in lettersGuessed for i in set(secretWord)])
    # OR
    # return set(secretWord) == (set(secretWord) & lettersGuessed)
    
    
            



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            secretWord = secretWord.replace(i, '_ ')
    return secretWord
    # List Comprehension
    # return ''.join([l if l in letterGuessed else '_ ' for l in secretWord])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join([letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in lettersGuessed])
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
                                                p;;;;;;;;;-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999============/'???????????                                                                                                                     
    * At the start of the [;'ppppppp'game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')

    lettersGuessed = []
    round = 8
    while round > 0:
        
        print(f"You have {round} guesses left.")
        print('Available letters:', getAvailableLetters(lettersGuessed))
        
        letter = input('Please guess a letter: ').lower()
        if letter in lettersGuessed:
            print("Opps! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print("------------------------------------")
            continue
        else:
            lettersGuessed.append(letter)
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("--------------------------------------")
            print("Congratulations, you won!")
            break
        else:
            if letter in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                print("------------------------------------")
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                print("------------------------------------")
            round -= 1
    if round == 0:
        print(f"Sorry, you ran out of guesses. The word was {secretWord}.")
                      
        


secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)
