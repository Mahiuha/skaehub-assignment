#importing the csv module
#converts the csv file into a dictionary
#prints the converted csv file as a dictionary.

import csv

#converts the csv file into a dictionary

with open('username.csv', newline='') as f:
    reader = csv.reader(f)
    data_list = list(reader)
print(data_list)
