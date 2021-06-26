
#imports the itertools library 
import itertools

#a list of names
name_list = ["Brian", "David", "joe", "Doe"]

#loops through the iterable infinitely
for element in itertools.cycle(name_list):
    print(element)