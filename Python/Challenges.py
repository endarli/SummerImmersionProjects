from random import*
level1 = randint(0, 6)
level2a = randint(0, 3)
level2b = randint(0, 3)
level2c = randint(0, 3)
#do ListName[index] to do that vv


#level1
Business = ["Moodys", "TD Bank", "Swell", "Apple", "Samsung", "Citi Group", "Lenovo"]
Names = ["Shirley", "Jendy", "Olivia", "Evolone", "Rianna", "Caroline", "Sara"]
Food = ["Oreos", "Ice Cream Sandwich", "Cronut", "Marshmallow", "Haribos", "Cannoli", "Strawberries"]

user_input = input("Type 'food', 'names', or 'businesses' to generate a name: ")
if user_input == "food":
    print("Your name is: ", Food[level1])
elif user_input == "names":
    print("Your name is: ", Names[level1])
elif user_input == "businesses":
    print("Your name is: ", Business[level1])
###################################################

#level2
sides = ["mac and cheese", "calamari", "fries", "kale salad"]
main = ["Salmon in a lemon butter sauce", "Mac and cheese", "Grilled chicken", "A portabello mushroom burger"]
dessert = ["ice cream", "watermelon", "tiramisu", "depression"]

user_input = input("Type 'yes' or 'no' if you want a menu for dinner.")
if user_input == "yes":
    print("Your dinner menu is: ", main[level2a], "with a side of", sides[level2b], "and", dessert[level2c], "for dessert.")
else:
    print("Whatever, you're getting one anyways.")
    print("Your dinner menu is: ", main[level2a], "with a side of", sides[level2b], "and", dessert[level2c], "for dessert.")
