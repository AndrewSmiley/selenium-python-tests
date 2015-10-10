__author__ = 'pridemai'
import unittest
from nose import *
from functions import hello, is_even
# class ParseTestCases(unittest.TestCase):
#         def __init__(self,*args,**kwargs):
#             # self.better_csv=BetterCSV()
#             super(ParseTestCases, self).__init__(*args, **kwargs)
#
def test1():
    assert is_even(4) == True
def test2():
    assert is_even(3) == False
def test3():
    assert is_even(5) == False