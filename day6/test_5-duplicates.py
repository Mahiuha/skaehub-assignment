import unittest
import duplicates

class testDuplicates(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(5-duplicates.dict_list),dict,"Should be dict")
    def test_type2(self):
        self.assertIs(type(5-duplicates.list_final),list)

if __name__=="__main__":
    unittest.main()