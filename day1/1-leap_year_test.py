# content of test_sysexit.py
# import pytest
# # content of test_sample.py
# def leap_year(x):
#     return x % 100 
# def not_leap_year(x):
#     return x % 4
# def year_is_int(x):
#     return int(x)    
# def test_leap_year():
#      assert leap_year(2000) == 0
# def test_not_leap_year():
#     assert not_leap_year(1999) > 0
def leap(year):
    if (year % 4 == 0) or (year % 100 != 0) and (year % 400 == 0):
        print(" % d is a leap year" % year)

    else:
        print(" % d is not a leap year" % year)

year = int(input("Enter the year you wish to check: "))

leap(year)
# def test_year_is_int():
#     assert year_is_int('w') > 0
 
# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 5

''' Joe  2:14 PM
Nice

Kahenyaa  3:14 PM
kwa year
3:14
year(2021)
3:15
def (year):
3:17
def word_length(statement):
    x = statement.split()
    last_word = x[-1]
    return len(last_word)
word_length('Django is a good dog')
3:18 '''
# import pytest
# import question2
# def word_length(a):
#     legth = question2.word_length(a)
#     return legth
# def test_word_legth():
#     assert word_length("Django is a good dogy") == 4
# def check_if_word_is_string():
#     word_length("Django is a good dogy")
#     legth = question2.word_length(a)
#     if (type(a) == str ):  
#         return 0
#     else:
#         return 1
# def test_if_word_is_string():
#     assert check_if_word_is_string == 1 
''' 3:21
import pytest
import question2
def word_length(a):
    legth = question2.word_length(a)
    return legth
def test_word_legth():
    assert word_length("Django is a good dogy") == 4

Kahenyaa  4:38 PM '''
# question 1: tests
# content of test_sysexit.py
''' import pytest
import question1
# content of test_sample.py
#test if year entered is integer
def year(x):
    leap_year = question1.year(x)
    return leap_year
def test_year():
    assert year(2012) > 0
#test of year is divisible by 100
def leap_year(x):
    leap_year = question1.leap_year(x)
    return leap_year
def test_leap_year():
    assert leap_year(2011) > 0
#if year is divisible by both 4 & 400 (non leap year)
def not_leap_year(x):
    not_leap_year = question1.not_leap_year(x)
    return not_leap_year   
def test_not_leap_year():
    assert not_leap_year(2011) == 1
#if year is divisible by both 4 & 400 (leap year)
def leap_year_4_and_400(x):
    not_leap_year = question1.not_leap_year(x)
    return not_leap_year  
def test_leap_year_4_and_400():
    assert not_leap_year(2000) == 0 '''