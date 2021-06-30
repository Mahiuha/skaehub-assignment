import unittest
import lastword

class testWord(unittest.TestCase):
    def setUp(self):
        self.word=lastword.word_input
        self.list=lastword.list

    def test_word(self):
        self.assertIs(type(self.word),str)

    #test if the text input is split into a string at separatorrs
    def test_list(self):
        self.assertEqual(type(self.list),list)

    def tearDown(self):
        return super().tearDown()

if __name__=="__main__":
    unittest.main()
