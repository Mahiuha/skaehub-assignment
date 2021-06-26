#imports sqrt from the math module
from math import sqrt

#prompt user for a number
square = int(input("Enter Number: "))

#find square root of user input number
square_root = sqrt(square)
print(square_root)

#if the number is a perfect square print true elase prints false
if( square == square_root*square_root):
   print (isinstance(square_root, int))
else:
    print (isinstance(square_root, int))