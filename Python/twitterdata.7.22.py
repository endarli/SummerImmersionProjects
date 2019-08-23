#prints out data from json file

import json

#opens json file
tweetFile = open("./twitterdata.7.22.json", "r")

#gets data from opened file
tweetData = json.load(tweetFile)

#closes file
tweetFile.close()

#0 stands for the first object, #id stands for the key
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("Tweet ID: ",tweetData[0]["id"])
print("Tweet text: ", tweetData[0]["text"])

#idx means were looking at the indexes in objects
for idx in range(len(tweetData)):
    print("Tweet id: ", tweetData[idx]["id"])

#you only need tweet[text] here because were not touching the indexes, were looking at the objects
for obj in tweetData:
    print("Tweet text: ", obj["text"])
