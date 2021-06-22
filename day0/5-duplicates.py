#create a list with duplicates
#using the fromkeys() function generate a dictionary from keys
#then convert the dictionary back into a list with no duplicate
#prints the new list

duplicates = ['joe', 'kevin', 'brian', 'titus', 'joe', 'bunny', 'brian', 'david']

print(list(set(duplicates)))
