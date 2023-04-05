import sys
import random
import datetime as dt
import os
import csv
import json
import re

# stuff = sys.argv
# print(f"Num of args passed: {len(stuff)}")

#Sample a list n number of times
list = [1 ,3 ,4,5]
selection = random.sample(list,4)
print(selection)

hour_now = dt.datetime.now().hour
hour_now2 = dt.datetime.hour
print(hour_now)
print(hour_now2)

# make_dir = os.mkdir("testing_paths")
list_dir = os.listdir("C:/Users/vodde/Desktop/Work Stuf/Cognixia Program/Week1")
print(list_dir)

#Open dbd data excel sheet, get headers
with open ("DBD Maps Data - Sheet1.csv", "rt") as csvfile:
    data = csv.reader(csvfile)
    headers = next(data)
    
print(headers)

#Json module
json_string = json.dumps(list)
print(json_string)

#Testing regex's
str1 = "acbx1"
str2 = "TOP@1"
str3 = "mAT$0"
str4 = "RUN#!"
regex = "[A-Z]{3}.[1-9]"

match = re.search(regex, str1)
print(match)
match2 = re.search(regex,str2)
print(match2)
match3 = re.search(regex,str3)
print(match3)
match4 = re.search(regex,str4)
print(match4)

#Change numbers in str to @ signs
my_str = "46501939helloworld"
print(re.sub('[0-9]', '@', my_str))



