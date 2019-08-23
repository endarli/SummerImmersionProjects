#make list
#ask for numbers
#add numbers to list
#find sum of numbers in list
#output the sum

list = []

def calc_total():
    print("Sum of your numbers:", sum(list))


def main():
    answer = int(input("Please give me a number: "))
    list.append(answer)
    while True:
        answer2 = input("Do you have any other numbers? Type 'yes' or 'no'. ")
        if answer2 == "yes":
            answer = int(input("Please give me another number: "))
            list.append(answer)
        elif answer2 == "no":
            calc_total()
            break

if __name__ == "__main__":
    main()
