# Update this text to match your story.

from random import*

number1 = randint(1,2)
number2 = randint(1,4)

for x in range(50):
    print(" ")

start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the wall: "You have 5 seconds to choose."
There is a door to your right and to your left.
'''

print(start)
print("As you walk down the hallway, you notice that there is a moldy lollipop on the ground.")

user_input = input("Type 'grab' to pick up the lollipop or 'ignore' to ignore the lollipop: ")

if user_input == "grab":
    lollipop = 1
else:
    lollipop = 0

print(" ")
user_input = input("Type 'left' to go left or 'right' to go right: ")

if user_input == "left":
    print(" ")
    print("You decide to go left and...") # Update to match your story.
    print("find an empty room, except for a red button on the wall.")
    user_input = input("Type 'yes' to press the button or 'no' to exit the room: ")

    if user_input == "yes":
        print(" ")
        print("***EXPLOSION***")
        print("YIKES. You were blown up by a bomb.")

    elif user_input == "no":
        print(" ")
        print("You try to turn the door knob, but it is locked.")
        print("An envelope is slipped under the door.")
        print("Do you open the envelope or ask 'Who's there?'")
        user_input = input("Type 'open' to open the envelope or 'ask' to ask who is there: ")

        if user_input == "open":
            print(" ")
            print("The envelope states 'The room is about to blow up. Take cover!'")
            print("***EXPLOSION***")

        elif user_input == "ask":
            print(" ")
            print("You ask 'Who is there?'")
            print("A minute passes.")
            print("Then you hear someone whisper 'Give me a lollipop and I'll open the door.'")

            if lollipop == 1:
                print(" ")
                print("You give them your lollipop.")

                if number1 == 1:
                    print(" ")
                    print("The person says 'Thank you for the lollipop. I'll open the door.")
                    print("He opens the door and you wake up from your dream within a dream.")
                    print("Your alarm goes off and you have to go to school now.")

                elif number1 == 2:
                    print(" ")
                    print("The person says 'Thank you for the lollipop. Good luck on your own.'")
                    print("You turn around dissappointed.")
                    print("***EXPLOSION***")
                    print("A day has passed.")
                    print("As a ghost, you watch your family mourn you death.")
                    print("The night before, they found your body cold and motionless in your bed.")

            else:
                print(" ")
                print("You look through your pockets and cannot find a lollipop.")
                user_input = input("Type 'beg' to beg the person for mercy or 'accept' to accept your fate: ")

                if user_input == "beg":
                    print(" ")
                    print("You begin to beg for mercy")

                    if number2 == 1:
                        print(" ")
                        print("The person feels sympathy for you and opens the door.")
                        print("He opens the door and you wake up from your dream within a dream.")
                        print("You wake up to the sound of birds chirping and go to the bathroom to get ready.")

                    else:
                        print(" ")
                        print("The person does not respond.")
                        print("***EXPLOSION***")
                        print("You look down and realize that you're a ghost. Your body is now transparent.")
                        print("As a ghost, you watch your family mourn you death.")
                        print("The night before, they found your body cold and motionless in your bed.")

                elif user_input == "accept":
                    print(" ")
                    print("You turn around dissappointed.")
                    print("***EXPLOSION***")
                    print("You look down and realize that you're a ghost. Your body is now transparent.")
                    print("As a ghost, you watch your family mourn you death.")
                    print("The night before, they found your body cold and motionless in your bed.")

elif user_input == "right":
    print(" ")
    print("You choose to go right and ...")
    print("the hallway changes to a thickly vined forest.")
    print("You see two trails.")
    user_input = input("Type 'concrete' to go on the concrete trail or 'gravel' to go on the gravel trail: ")

    if user_input == "concrete":
        print(" ")
        print("You begin to walk down the conrete road and suddenly trip on a rock.")
        user_input = input("Type 'clean' to clean off the scab on your knee or 'ignore' to keep walking down the road: ")

        if user_input == "clean":
            print(" ")
            print("You clean off the scab and continue walking down the road.")
            print("As you continue your journey, you hear high pitched cries from a baby on the side of the road.")
            user_input = input("Type 'help' to help the baby or 'ignore' to ignore it's distressing cries: ")

            if user_input == "help":
                print(" ")
                print("You walk over and kneel down to save the baby from the mass of bloody, dead bodies on the dirty road.")

                if number2 == 2:
                    print(" ")
                    print("As you get up, you feel a sharp pain coming from your leg.")
                    print("Soon, as you walk down the road with the now calm baby, the feeling spreads to the rest of your body.")
                    print("You feel numbness as well and your legs are slowly giving way.")
                    print("It turns out you were infected by the same disease that killed all of the people before.")

                else:
                    print(" ")
                    print("The baby calms down immediately and gives you the most adorable smile you've ever seen.")
                    print("You're glad you saved her and the two of you continue down the road home.")

            elif user_input == "ignore":
                print(" ")
                print("As you go down the road, you trip again but this time, on a dead body.")
                print("As you get up, you feel a sharp pain coming from your leg.")
                print("You feel numbness as well and your legs are slowly giving way.")
                print("It turns out you were infected by the same disease that killed all of the people before.")

        elif user_input == "ignore":
            print(" ")
            print("As you go down the road, you trip again but this time, on a dead body.")
            print("As you get up, you feel a sharp pain coming from your leg.")
            print("You feel numbness as well and your legs are slowly giving way.")
            print("It turns out you were infected by the same disease that killed all of the people before.")

    if user_input == "gravel":
        print(" ")
        print("You find a white unicorn with the softest mane.")
        user_input = input("Type 'mount' to get on the unicorn or 'ignore' to continue walking, but also pet the mane because it is so fluffy: ")

        if user_input == "mount":
            print(" ")
            print("You get on the unicorn and begin to gallop down the road with it.")
            print("Soon, a bright light flashes before your eyes.")
            print("It turns out you were in a dream, and you get up from bed to go brush your teeth.")

        elif user_input == 'ignore':
            print(" ")
            print("You continue down the road and see many more unicorns.")
            print("You pet them happily for a long while.")
            print("You accidentally trip on a rock and wake up from your dream.")
            print("It is morning and you have work, today.")
