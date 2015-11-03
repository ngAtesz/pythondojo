import unittest
from RomanNumeralKata.roman_numeral import RomanNumeral

class RomanNumeralTest(unittest.TestCase):
    def test_zero(self):
        rn = RomanNumeral()
        self.assertEqual("", rn.arabic_to_roman(0))

if __name__ == "__main__":
    unittest.main()