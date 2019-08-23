f = open("dict.txt","r")

print("Can your password survive a dictionary attack?")
test_password = input("Type in a trial password: ")
test_password = test_password.lower().split()

for word in f:
    if word == test_password:
        print("Your passwword would not survive!")
        break
    else:
        print("Your password would survive!")
        break
