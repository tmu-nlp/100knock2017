import unittest
from knock71 import is_stopword

class Testistopword(unittest.TestCase):
    def test_check_the(self):
        self.assertTrue(is_stopword('the'))

    def test_check_a(self):
        self.assertTrue(is_stopword('a'))

    def test_check_i(self):
        self.assertTrue(is_stopword('i'))

    def test_check_you(self):
        self.assertTrue(is_stopword('you'))

    def test_check_nlp(self):
        self.assertFalse(is_stopword('nlp'))

    def test_check_physics(self):
        self.assertFalse(is_stopword('physics'))

    def test_check_no_args(self):
        # 引数なしのときはraise TypeError
        with self.assertRaises(TypeError):
            is_stopword()
    
    def test_check_zerolength(self):
        with self.assertRaises(TypeError):
            is_stopword('')

if __name__ == '__main__':
    unittest.main()
