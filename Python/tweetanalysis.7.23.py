'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

polar= []
subject= []

#Get the JSON data
tweetFile = open("./twitterdata.7.22.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


#finds polarity of texts
for obj in tweetData:
    print()
    x = TextBlob(obj["text"])
    print("Tweet text: ", obj["text"])
    if x.polarity > 0:
        print("Subjectivity: ", x.polarity)
        subject.append(float(x.polarity))
    if x.polarity < 0:
        print("Polarity: ", x.polarity)
        polar.append(float(x.polarity))
    if x.polarity == 0:
        print("This statement is neutral.")

print("Average of Negative statements:", sum(polar)/len(polar))
print("Average of Positive statements:", sum(subject)/len(subject))

print(" ")
print("This is your Polar trend graph: ")
# the histogram of the data
plt.hist(polar, 3)
plt.xlabel('Polarity')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Polarity')
plt.show()

print(" ")
print("This is your Polar trend graph: ")
# the histogram of the data
plt.hist(subject, 5)
plt.xlabel('Subjectivity')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Subjectivity')
plt.show()
