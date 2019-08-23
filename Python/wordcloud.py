#from wordcloud import WordCloud
import json
from textblob import TextBlob
import numpy as np

#Get the JSON data
tweetFile = open("./twitterdata.7.22.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

list = []
for obj in tweetData:
    x = TextBlob(obj["text"])
    list.append(str(x))

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

', '.join(list)
stringy = str(list)
print(stringy)

print("Hello")
print(" ")
print(" ")
print(" ")
print(" ")
