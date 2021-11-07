import unittest
import main
from fraction import Fraction

class TestParser(unittest.TestCase):
    
    def test_simple_parse(self):
        a = main.parse("0_1/2 + 0_1/2")
        b = Fraction("1_0/1")
        self.assertEqual(a, b)
