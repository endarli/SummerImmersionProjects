#nonsense = {
#    'hola' : 'hello',
#    'bob' : 'funny man',
#    'number' : '30' '40'
#    }
#print(nonsense)

#anyeonghaseo = nonsense['hola']
#print(anyeonghaseo)

#nonsense['doggo'] = 'cute dog'
#print(nonsense)

#num = nonsense['number']
#print(int(num))

# Creates the dictionary to store responses.


answersu1 = {}
answersu2 = {}
answersu3 = {}
answersu4 = {}
ages = []
hrs = []
path = './'
fileName = 'Survey.json'
import json
import time

def dictionaryToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def u1():
    print("You are the 1st participant!")
    a1 = input("What is your name? ")
    answersu1['user'] = a1
    a2 = input("How old are you? ")
    answersu1['age'] = a2
    a3 = input("How many hours do you spend on your phone a day? ")
    answersu1['hrs spent on phone per day'] = a3
    a4 = input("Name the app you use most frequently. ")
    answersu1['most used app'] = a4
    a5 = input("Where do you call home? ")
    answersu1['home'] = a5
    print("Here are your survey answers!")
    print(answersu1)
    print(" ")
    print(" ")

def u2():
    print("You are the 2nd participant!")
    a1 = input("What is your name? ")
    answersu2['user'] = a1
    a2 = input("How old are you? ")
    answersu2['age'] = a2
    a3 = input("How many hours do you spend on your phone a day? ")
    answersu2['hrs spent on phone per day'] = a3
    a4 = input("Name the app you use most frequently. ")
    answersu2['most used app'] = a4
    a5 = input("Where do you call home? ")
    answersu2['home'] = a5
    print("Here are different people's survey answers!")
    print(answersu1)
    print(answersu2)
    print(" ")
    print(" ")

def u3():
    print("You are the 3rd participant!")
    a1 = input("What is your name? ")
    answersu3['user'] = a1
    a2 = input("How old are you? ")
    answersu3['age'] = a2
    a3 = input("How many hours do you spend on your phone a day? ")
    answersu3['hrs spent on phone per day'] = a3
    a4 = input("Name the app you use most frequently. ")
    answersu3['most used app'] = a4
    a5 = input("Where do you call home? ")
    answersu3['home'] = a5
    print("Here are different people's survey answers!")
    print(answersu1)
    print(answersu2)
    print(answersu3)
    print(" ")
    print(" ")

def u4():
    print("You are the 4th participant!")
    a1 = input("What is your name? ")
    answersu4['user'] = a1
    a2 = input("How old are you? ")
    answersu4['age'] = a2
    a3 = input("How many hours do you spend on your phone a day? ")
    answersu4['hrs spent on phone per day'] = a3
    a4 = input("Name the app you use most frequently. ")
    answersu4['most used app'] = a4
    a5 = input("Where do you call home?")
    answersu4['home'] = a5
    print("Here are different people's survey answers!")
    print(answersu1)
    print(answersu2)
    print(answersu3)
    print(answersu4)

def math():
    print("Above are the ages of people and times people spent on their phones.")
    age1 = input("Please type the age of the first person: ")
    ages.extend(age1)
    age2 = input("Please type the age of the second person: ")
    ages.extend(age2)
    age3 = input("Please type the age of the third person: ")
    ages.extend(age3)
    age4 = input("Please type the age of the fourth person: ")
    ages.extend(age4)

    hr1 = input("Please type the hours on the phone of the first person: ")
    hrs.extend(hr1)
    hr2 = input("Please type the hours on the phone of the second person: ")
    hrs.extend(hr2)
    hr3 = input("Please type the hours on the phone of the third person: ")
    hrs.extend(hr3)
    hr4 = input("Please type the hours on the phone of the fourth person: ")
    hrs.extend(hr4)
    time.sleep(2)

def main():
    print("Hi, this is a survey involving three people!")
    u1()
    time.sleep(3)
    u2()
    time.sleep(3)
    u3()
    time.sleep(3)
    u4()

    dictionaryToJson(path, fileName, answersu1)
    dictionaryToJson(path, fileName, answersu2)
    dictionaryToJson(path, fileName, answersu3)
    dictionaryToJson(path, fileName, answersu4)

    math()
    avgage = sum(int(ages))/len(int(ages))
    print("Average age of people that took the survey:", avgage)
    avghrs = sum(hrs)/len(hrs)
    print("Average hours spent on phone of people that took the survey: ", avghrs)
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
