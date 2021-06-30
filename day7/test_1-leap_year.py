# content of test_sysexit.py
import pytest
import leap_year1


# content of test_sample.py

#test if year entered is integer
def year(x):
    leap_year = leap_year1.year(x)
    return leap_year

def test_year():
    assert year(2012) > 0


#test of year is divisible by 100
def leap_year(x):
    leap_year = leap_year1.leap_year(x)
    return leap_year

def test_leap_year():
    assert leap_year(2011) > 0

#if year is divisible by both 4 & 400 (non leap year)
def not_leap_year(x):
    not_leap_year = leap_year1.not_leap_year(x)
    return not_leap_year   

def test_not_leap_year():
    assert not_leap_year(2012) == 1

#if year is divisible by both 4 & 400 (leap year)
def leap_year_4_and_400(x):
    not_leap_year = leap_year1.not_leap_year(x)
    return not_leap_year  

def test_leap_year_4_and_400():
    assert not_leap_year(2000) == 0


