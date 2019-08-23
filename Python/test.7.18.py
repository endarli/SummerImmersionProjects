import time
from random import*

# --- Define your functions below! ---

yesresp = ["yes", "sure", "yea", "yeah", "mhm", "Yes", "Yea", "Sure", "Yeah", "Mhm", "yurr", "Yurr", "ok", "okay", "Ok", "Okay", "yesss", "yea gurl", "yea sis", "yes sis"]
noresp = ["no", "nah", "nope", "I don't think so", "idts", "Do I look like", "No", "Nah", "Nope", "do i look like", "bro", "bruh", "Bro", "Bruh", "imma beep boop outta here"]

def intro():
    print("Hi, my name is Chatbot.")
    answer = input("What's your name? ")
    print(" ")
    print("Hi", answer, ", how are you? ")

def process(b):
    print("'", b, "' You say?", "Great!")
    print(" ")

def poem(a):
    if a in yesresp:
        print("Yay!")
        print("Hmm... Let me think of something.")
        time.sleep(3)
        print("When someone's having a bad day,")
        print("A smile could go a long way,")
        print("So make sure to put one on")
        print("And keep it until the day is gone.")
        print(" ")
    elif a in noresp:
        print("Aw. :(")
        print(" ")

def art(d):
    if d in yesresp:
        time.sleep(1)
        print("Yay!")
        print(".-. .-')                            ,---. ")
        print("\  ( OO )                           |   | ")
        print(" ;-----.\  .-'),-----.  .-'),-----. |   | ")
        print(" | .-.  | ( OO'  .-.  '( OO'  .-.  '|   | ")
        print(" | '-' /_)/   |  | |  |/   |  | |  ||   | ")
        print(" | .-. `. \_) |  |\|  |\_) |  |\|  ||  .' ")
        print(" | |  \  |  \ |  | |  |  \ |  | |  |`--'  ")
        print(" | '--'  /   `'  '-'  '   `'  '-'  '.--.  ")
        print(" `------'      `-----'      `-----' '--'  ")
    elif d in noresp:
        print("Aw :(")

def rps(y):
    comp = randint(0,2)
    if comp == 0:
        comp = "rock"
    elif comp == 1:
        comp = "paper"
    elif comp == 2:
        comp = "scissor"

    if y in yesresp:
        print("Yay!")
        time.sleep(1)
        answer = input("rock, paper, scissor, and shoot! ")
        if answer == comp:
            print("We tied!")

        elif answer == "rock":
            if comp == "scissor":
                print("I shot scissor. You win!")
            elif comp == "paper":
                print("I shot paper. I win!")

        elif answer == "paper":
            if comp == "scissor":
                print("I shot scissor. I win!")
            elif comp == "rock":
                print("I shot rock. You win!")

        elif answer == "scissor":
            if comp == "rock":
                print("I shot rock. I win!")
            elif comp == "paper":
                print("I shot paper. You win!")
    if y in noresp:
        print("Aw :(")

# --- Put your main program below! ---
def main():
    intro()
    answer = input(" ")
    process(answer)
    time.sleep(1)
    answer2 = input("Do you want to hear a poem? ")
    poem(answer2)
    time.sleep(1)
    answer3 = input("Wanna see some cool art? ")
    art(answer3)
    answer4 = input("Wanna play rock paper scissor? ")
    rps(answer4)
    answer5 = input("Wanna play again? ")
    while answer5 in yesresp:
        rps(answer5)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
