#  nested if and modulas

def year(x):
        
    return x


def leap_year(x):
    leap = x%100
    #print ('Leap Year',leap)
    return leap

def not_leap_year(x):
    test = x%4
    test1 = x%400
    if (test == test1):
        leap = 0
        print(leap)
        return leap
    else:
        leap = 1
        print(leap)
        return leap

year(2021)
leap_year(2021)
not_leap_year(2011)


