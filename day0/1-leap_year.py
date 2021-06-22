#prompt user for input in this case year
#define a function like leap
#check if the year is divisible by 4 and 400 then it is a leap year 
#if either of the condition above is false or if is divisible by 100 then the year is not a leap year
#finally print out the feedback to the user
#call the function you declared

year = int(input("Enter the year you wish to check: "))

def leap(year):
    if((year%4 == 0)or(year%100 != 0)and(year%400 == 0)):
        print("%d is a leap year"%year)
    else:
        print("%d is not a leap year"%year)
leap(year)
