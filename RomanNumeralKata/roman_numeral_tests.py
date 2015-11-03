import unittest
from RomanNumeralKata.roman_numeral import RomanNumeral


class RomanNumeralTest(unittest.TestCase):
    def test_zero(self):
        rn = RomanNumeral()
        self.assertEqual("", rn.arabic_to_roman(0))

    def test_one(self):
        rn = RomanNumeral()
        self.assertEqual("I", rn.arabic_to_roman(1))

    def test_five(self):
        rn = RomanNumeral()
        self.assertEqual("V", rn.arabic_to_roman(5))

    def test_two(self):
        rn = RomanNumeral()
        self.assertEqual("II", rn.arabic_to_roman(2))

    def test_eight(self):
        rn = RomanNumeral()
        self.assertEqual("VIII", rn.arabic_to_roman(8))

    def test_four(self):
        rn = RomanNumeral()
        self.assertEqual("IV", rn.arabic_to_roman(4))


if __name__ == "__main__":
    unittest.main()
