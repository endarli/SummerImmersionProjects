import labor
list_of_result = labor.get_results()

import sys as _sys
import os as _os
import json as _json
import sqlite3 as _sql
import difflib as _difflib

from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

Employedw = []
Unemployedw = []
Employedb = []
Unemployedb = []


print(list_of_result[1])

for obj in range(len(list_of_result)):
    print("Employed Whites: ", list_of_result[obj]["Data"]["Employed"]["White"]["Counts"]["All"])
    Employedw.append(list_of_result[obj]["Data"]["Employed"]["White"]["Counts"]["All"])
    print("Unemployed Whites: ", list_of_result[obj]["Data"]["Unemployed"]["White"]["Counts"]["All"])
    Unemployedw.append(list_of_result[obj]["Data"]["Unemployed"]["White"]["Counts"]["All"])

for obj in range(len(list_of_result)):
    print("Employed Blacks: ", list_of_result[obj]["Data"]["Employed"]["Black or African American"]["Counts"]["All"])
    Employedb.append(list_of_result[obj]["Data"]["Employed"]["Black or African American"]["Counts"]["All"])
    print("Unemployed Blacks: ", list_of_result[obj]["Data"]["Unemployed"]["Black or African American"]["Counts"]["All"])
    Unemployedb.append(list_of_result[obj]["Data"]["Unemployed"]["Black or African American"]["Counts"]["All"])


Whites = [[Employedw], [Unemployedw]]
Blacks = [[Employedb], [Unemployedb]]

print(" ")
print("These are your graphs: ")
# the histogram of the data
plt.hist(Employedw, 12)
plt.xlabel('Number of Employed People')
plt.ylabel('Frequency')
plt.title('Histogram of Employed Whites')
plt.show()

print(" ")
# the histogram of the data
plt.hist(Unemployedw, 12)
plt.xlabel('Number of Unemployed People')
plt.ylabel('Frequency')
plt.title('Histogram of Unemployed Whites')
plt.show()

print(" ")
# the histogram of the data
plt.hist(Employedb, 12)
plt.xlabel('Number of Employed People')
plt.ylabel('Frequency')
plt.title('Histogram of Employed Blacks')
plt.show()

print(" ")
# the histogram of the data
plt.hist(Unemployedb, 12)
plt.xlabel('Number of Unemployed People')
plt.ylabel('Frequency')
plt.title('Histogram of Unemployed Blacks')
plt.show()

######################################################

import pandas
from collections import Counter

letter_counts = Counter(Employedw)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')
