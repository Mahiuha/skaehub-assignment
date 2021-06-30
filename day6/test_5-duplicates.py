import unittest
import duplicates
from duplicates import *

class testDuplicates(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(duplicates.read),dict,"Should be dict")
    def test_type2(self):
        self.assertIs(type(duplicates.read),list)

if __name__=="__main__":
    unittest.main()