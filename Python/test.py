# This is a comment
# Python doesn't read
# what goes here.

# go to the directory and do
# python [name of doc]
# to run this code

#7/15/2019

# task 1
#print("Hello, World!")
#print("Woah")

#task 2
#answerr = input("What is your name?")
#print("Hello", answerr, "!")
#answer = input("Who inspires you?")
#print(answer, "inspires you!")

#task 3
#i = -1
#while True:
#    i += 1
#    if(i > 20):
#        break
#    if(i % 2 != 0):
#        continue
#    print(i)

#task 4
#imports the ability to get a random number
#(we will learn more about this later!)
from random import *

#Generates a random integer.
aRanNum = randint(1, 30)
# For Testing: print(aRandomNumber)
tries = 0
while tries < 2:
    guess = input("Guess a number between 1 and 30 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    	print("That's not a positive whole number; you've broken my code!")
    else:
    	guess = int(guess) # converts a string to an integer

    if(guess != aRanNum):
        if(guess < aRanNum):
            print("Try a little higher!")
        else:
            print("Try a little lower!")
        tries += 1
    else:
        print("You guessed the right number!")
        break
if(tries == 2):
    guess = input("Guess a number between 1 and 30 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    	print("That's not a positive whole number, you've broken my code!")
    else:
    	guess = int(guess) # converts a string to an integer

    if(guess < aRanNum):
        print("Sorry, your number was too low and you ran out of tries!")
    elif(guess > aRanNum):
        print("Sorry, your number was too high and you ran out of tries!")
    else:
        print("Yay! You guessed the right number!")
