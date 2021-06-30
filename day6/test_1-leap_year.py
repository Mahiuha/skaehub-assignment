import unittest
from unittest.case import TestCase
from year import *

class is_leap_year(unittest.TestCase):
    #year = int(input("Enter year: "))

    def  divisible_by_4(self):
        #year = int(input("Enter year: "))
        self.assertEqual(year%4 & year%400, 0)

    def divisible_by_100(self):
        #year = int(input("Enter year: "))
        self.assertEqual(year%100, 0)
        
    def divisible_by_400(self):
        #year = int(input("Enter year: "))
        self.assertEqual(year%400, 0)

if __name__ == '__main__':
    unittest.main()
        
    