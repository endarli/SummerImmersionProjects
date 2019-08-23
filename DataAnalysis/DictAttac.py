#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:

f = open("dict.txt","r")


print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:
isitin = False

while test_password in f(read):
    isitin = True
    if isitin == True:
        print("Your password would not survive a dictionary attack! Be careful!")
    break

if isitin == False:
    print("Yay, your password would survive a dictionary attack!")



#another way

for word in f:
    if word == test_password.split().lower():
        print("Your passwword would not survive!")
    else:
        print("Your password would survive!")
