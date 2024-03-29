# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if(i not in lettersGuessed):
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ""
    for i in secretWord:
        if(i not in lettersGuessed):
            string += ' _ '
        else:
            string += i
    return string



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    result = string.ascii_lowercase
    
    for i in lettersGuessed:
        newResult = result.replace(i, '')
        result = newResult
    return result
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    numGuesses = 8
    lettersGuessed = []
    print("-----------")
    
    while(numGuesses > 0):
        print("You have " + str(numGuesses) + " guesses left")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        
        val = input("Please guess a letter: ")
        
        
        if((val in secretWord) and (val not in lettersGuessed)):
            # In the word and not a repeated letter
            lettersGuessed.append(val)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif(val in lettersGuessed):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(val)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            numGuesses -= 1
        
        print("-----------")            
        if(isWordGuessed(secretWord, lettersGuessed) == True):
            print("Congratulations, you won!")
            break
        
    if(isWordGuessed(secretWord, lettersGuessed) == False):
        print("Sorry, you ran out of guesses. The word was " + secretWord)
            

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
