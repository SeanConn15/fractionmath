import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    
    def test_simple_add(self):
        a = Fraction(0, 1, 4)
        b = Fraction(0, 1, 4)
        res = Fraction(0, 1, 2) 
        a.add(b)
        self.assertEqual(a, res)

    def test_whole_rollover(self):
        a = Fraction(0, 1, 2)
        b = Fraction(0, 1, 2)
        res = Fraction(1, 0, 1) 
        a.add(b)
        self.assertEqual(a, res)

    def test_simplification(self):
        a = Fraction(0, 2, 4)
        b = Fraction(0, 1, 2)
        self.assertEqual(a, b)

    def test_parsing(self):
        a = Fraction("0_1/2")
        b = Fraction(0, 1, 2)
        self.assertEqual(a, b)
