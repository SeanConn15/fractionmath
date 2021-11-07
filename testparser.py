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
