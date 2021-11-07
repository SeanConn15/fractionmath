import unittest
import main
from fraction import Fraction

class TestParser(unittest.TestCase):
    
    def test_add(self):
        a = main.parse("0_1/2 + 0_1/2")
        b = Fraction("1_0/1")
        self.assertEqual(a, b)

    def test_subtract(self):
        a = main.parse("0_1/2 - 0_1/2")
        b = Fraction("0_0/1")
        self.assertEqual(a, b)

    def test_multiply(self):
        a = main.parse("0_1/2 * 0_1/2")
        b = Fraction("0_1/4")
        self.assertEqual(a, b)

    def test_divide(self):
        a = main.parse("0_1/2 / 0_1/2")
        b = Fraction("1_0/1")
        self.assertEqual(a, b)

    def test_normal_fraction(self):
        a = main.parse("1/2 + 0_1/2")
        b = Fraction("1_0/1")
        self.assertEqual(a, b)

    def test_example_1(self):
        a = main.parse("1/2 * 3_3/4")
        b = Fraction("1_7/8")
        self.assertEqual(a, b)

    def test_example_2(self):
        a = main.parse("2_3/8 + 9/8")
        b = Fraction("3_1/2")
        self.assertEqual(a, b)
