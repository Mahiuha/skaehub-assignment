import unittest
import password_generator

class password_gen(unittest.TestCase):
    def setUp(self):
        self.option=password_generator.opt
    def test_opt(self):
        self.assertIn(self.option,[1,2,3],"should be 1,2,3")



if __name__=="__main__":
    unittest.main()
