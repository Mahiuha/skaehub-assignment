
#first import the library numpy
#prompt user for an array of five numbers
#print out the memory occupied by the array back to the user as output 

import numpy as np

numbers_array = np.array([input("Input a number: ") for i in  range(5)])
#n = np.array([1, 2, 3, 4, 5])

print("original array: ")
print(numbers_array)
print('SIze of memory occupied: ')
print('%d bytes' %(numbers_array.size * numbers_array.itemsize))
