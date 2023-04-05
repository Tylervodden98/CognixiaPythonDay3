import csv
import json
import datetime as dt
import os

# Check if csv file exists if it does, format the list into dictionary using dictionary comprehension
if os.path.isfile("./employees.csv"):
    with open("employees.csv", "r") as data_employee:
        data = data_employee.readlines()
        print(data)
        dict_user = {data[i].split(":")[0]: data[i].split(
            ":")[1].replace("\n", "") for i in range(0, len(data))}
        print(dict_user)
else:
    # If csv file doesnt exist check if json file exists get data from it
    if os.path.isfile("./employees.json"):
        with open("employees.json", "r") as data_json:
            dict_user = json.load(data_json)
    else:
        # If both csv and json file don't exist we ask the user for the data
        dict_user = {}
        # Ask user for their entries to the dictionary
        dict_user["name"] = input("Please enter your name: ").capitalize()
        dict_user["age"] = int(input("Please enter your age: "))
        dict_user["years coding"] = int(
            input("Please enter your amount of years coding: "))
        birthday_info = input(
            "Please enter your birthday in 'YYYY' 'MM' 'DD' seperated by spaces: ")
        birthday_dates = birthday_info.split(" ")
        birthday = dt.datetime(
            year=int(birthday_dates[0]), month=int(birthday_dates[1]), day=int(birthday_dates[2]))
        dict_user["birthday"] = birthday

        # Ask for their first three programming languages as tuple
        languages = []
        for num in range(1, 4):
            languages.append(
                input(f"Enter {num} of 3 of your first coding languages: ").capitalize())
        tuple_language = tuple(languages)

        # Ask for their 3 favourite coding languages as list
        favorite_language = []
        for num in range(1, 4):
            favorite_language.append(
                input(f"Enter {num} of 3 of your favorite coding languages: ").capitalize())

        # Create a set that is an intersection of first 3 languages, and favorite languages

        language_intersection = list(set(languages) & set(favorite_language))

        # Add all the collections to the dictionary
        dict_user["first_languages"] = languages
        dict_user["favorite_languages"] = favorite_language
        dict_user["language_intersection"] = language_intersection

        # Open file and write to employees.csv
        with open("employees.csv", "wt") as employee:
            for key, value in dict_user.items():
                employee.write(f"{key}:{value}\n")

        # Open file and write to employees.json
        with open("employees.json", "wt") as employee_json:
            # dump dict_user dictionary as json string
            json.dump(dict_user, employee_json, default=str)

for pairs in dict_user.items():
    print(f"{pairs[0]} = {pairs[1]}")
