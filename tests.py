import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    
    def test_simple_add(self):
        a = Fraction(0, 1, 4)
        b = Fraction(0, 1, 4)
        res = Fraction(0, 1, 2) 
        a.add(b)
        self.assertEqual(a, res)

    def test_add_whole_rollover(self):
        a = Fraction(0, 1, 2)
        b = Fraction(0, 1, 2)
        res = Fraction(1, 0, 1) 
        a.add(b)
        self.assertEqual(a, res)

    def test_simplification(self):
        a = Fraction(0, 2, 4)
        b = Fraction(0, 1, 2)
        self.assertEqual(a, b)

    def test_simple_subtract(self):
        a = Fraction(0, 1, 2)
        b = Fraction(0, 1, 4)
        res = Fraction(0, 1, 4) 
        a.subtract(b)
        self.assertEqual(a, res)

    def test_subtract_rollunder(self):
        a = Fraction(0, 1, 4)
        b = Fraction(0, 1, 2)
        res = Fraction(0, -1, 4) 
        a.subtract(b)
        self.assertEqual(a, res)

    def test_subtract_whole_rollunder(self):
        a = Fraction(1, 0, 1)
        b = Fraction(0, 1, 2)
        res = Fraction(0, 1, 2) 
        a.subtract(b)
        self.assertEqual(a, res)

    # this tests to make sure handling negatives works correctly
    def test_negative_complex(self):
        a = Fraction(-1, 0, 1)
        b = Fraction(0, -1, 2)
        res = Fraction(-1, 1, 2) 
        a.subtract(b)
        self.assertEqual(a, res)


    def test_simple_multiply(self):
        a = Fraction(0, 1, 4)
        b = Fraction(0, 1, 2)
        res = Fraction(0, 1, 8) 
        a.multiply(b)
        self.assertEqual(a, res)

    def test_negative_multiply(self):
        a = Fraction(0, -1, 4)
        b = Fraction(0, 1, 2)
        res = Fraction(0, -1, 8) 
        a.multiply(b)
        self.assertEqual(a, res)

    def test_simple_divide(self):
        a = Fraction(0, 1, 2)
        b = Fraction(0, 1, 2)
        res = Fraction(1, 0, 1) 
        a.divide(b)
        self.assertEqual(a, res)


    def test_negative_constructor(self):
        a = Fraction(0, -1, 4)
        b = Fraction(0, 1, 4)
        self.assertNotEqual(a, b)


    def test_parsing(self):
        a = Fraction("0_1/2")
        b = Fraction(0, 1, 2)
        self.assertEqual(a, b)

    def test_parsing_with_whole(self):
        a = Fraction("1_1/4")
        b = Fraction(1, 1, 4)
        self.assertEqual(a, b)

    def test_negative_parsing(self):
        a = Fraction("0_-1/2")
        b = Fraction(0, -1, 2)
        self.assertEqual(a, b)
