#Secret Word
#make list of potential lowercase words and empty guess list
#make variables for fails
#choose random word from list
#display how many letters are in the word
#have them guess a letter
#if wrong, then add a fail and add letter to failed guess list
#if right, display which index the word is in and add to guess list
#repeat process until no more fails or full word guessed
###############################################################################

import random
#from random import*
# or  word = randint(0, 6)
maxfails = 9
fails = 0
gs = 0
guesses = []
failedg = []
potential_words = ["example", "words", "description", "dictionary", "projector"]

word = random.choice(potential_words)
word = list(word)

print("Number of letters in the word: ", len(word))
print("Possible amount of fails: ", maxfails)

while fails < maxfails:
    guess = input("Guess a letter: ")
    if guess in word:
        guesses.append([word.index(guess), guess], )
        guesses.sort()
        print("Letters guessed and their index #s: ", guesses)
        print("Failed letters guessed: ", failedg)
        gs += 1
        if gs > 1:
            if len(guesses) == len(word):
                print("Yay! You guessed the word!")
                break
    elif guess == "exit":
        break
#    elif len(split.guesses()) == len(word):
#        print("Yay! You guessed the word.")
    else:
        fails += 1
        failedg.append(guess, )
        print("Letters guessed and their index #s: ", guesses)
        print("Failed letters guessed: ", failedg)
    print("You have " + str(maxfails - fails) + " failed tries left!")
