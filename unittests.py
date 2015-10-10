__author__ = 'pridemai'
import unittest
from functions import hello, is_prime
class ParseTestCases(unittest.TestCase):
        def __init__(self,*args,**kwargs):
            # self.better_csv=BetterCSV()
            super(ParseTestCases, self).__init__(*args, **kwargs)

        def test1(self):
            self.assertEqual(is_prime(4), True)
        def test2(self):
            self.assertEqual(is_prime(3), False)
        def test3(self):
            self.assertEqual(is_prime(5), False)