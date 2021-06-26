#a simple dictionary
my_dict = {2: 10, 1: 2, -3: 1234}
 
#sorts my_dict using lambda
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))
print(sorted_dict)

