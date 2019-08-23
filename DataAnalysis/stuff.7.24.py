import school_scores
list_of_record = school_scores.get_all()

'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
import sys as _sys
import os as _os
import json as _json
import sqlite3 as _sql
import difflib as _difflib

from textblob import TextBlob

#print(list_of_record)
_test_interfaces()


#finds polarity of texts
for obj in school_scores:
    x = TextBlob(obj["'Average GPA'"])
    print("Average GPA: ", obj["text"])

for i in range(len(List)):
    print(List[i])
#prints what is in your list separately

for num in List:
    print(num)

#print("Average of Negative statements:", sum(polar)/len(polar))
#print("Average of Positive statements:", sum(subject)/len(subject))
