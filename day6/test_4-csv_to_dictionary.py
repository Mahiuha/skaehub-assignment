import csv_to_dictionary
import unittest

class Testcsvdictionary(unittest.TestCase):

   
    # read csv test 
    def test_read_csv(self):
        self.assertIsNotNone(4-csv_to_dictionary.read("peeps.csv"))

    # file not found test
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            4-csv_to_dictionary.read("")

    # test if correct type
    def test_if_correct_type(self):
        with self.assertRaises(OSError):
            4-csv_to_dictionary.read(6)
    

    
if __name__ == '__main__':
    unittest.main()