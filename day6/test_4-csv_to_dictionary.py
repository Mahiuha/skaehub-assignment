import unittest
import csv_to_dictionary
from csv_to_dictionary import *

class Testcsvdictionary(unittest.TestCase):

   
    # read csv test 
    def test_read_csv(self):
        self.assertIsNotNone(csv_to_dictionary.f("username.csv"))

    # file not found test
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            csv_to_dictionary.f("")

    # test if correct type
    def test_if_correct_type(self):
        with self.assertRaises(OSError):
            csv_to_dictionary.f(6)
    

    
if __name__ == '__main__':
    unittest.main()