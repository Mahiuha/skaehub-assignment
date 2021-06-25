#define a function which takes n as an argument

#declare a variable number and which stores the user input
number = int(input('Enter Number: '))

#this checks if the number provided when devided by four doesnt have a 
#remainder then prints is a power of four. 
if (number%4 == 0):
    print(number, 'is a power of 4')

#if the number returns a remainder when devided by four 
# then it tells the user it is not a poer of 4
else:
    print(number , 'is not a power of 4')
