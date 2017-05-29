#DESCRIPTION: Hangman game

import string
string.ascii_letters

#Welcome sentence
print("\nWelcome to Hangman! User 1, type in a word to continue.\n")

#User 1 inputs a word
import getpass      #Makes the typed word invisible
Secret = getpass.getpass("Type the secret word: ")

#Extend the input word into an array where each letter is a unique element
char_Secret = []        #Why do we input this first?
for line in Secret.upper():     #.upper() so that it creates a uniform text capitalization
    char_Secret.extend(line)
nSecret = len(char_Secret)

import sys
for nSecret in char_Secret:
    sys.stdout.write("\033[4m_\033[0m ")        #Prints number of underlined array cells on the same line

#User 2 inputs a letter to guess
print("\n\nThe secret word has now been entered. User 2, make your first guess!\n")

Guess = set(input("Guess a letter: ")) #str to set

#Tests if the letter is in the word. If so, where in the word the letter is located.
if Guess in char_Secret:
    for letter in char_Secret:
        if Guess & set(letter):
            sys.stdout.write(letter)
        else:
            print(" _ ")
else:
    print("*Head*")
