from CyberFizzBuzz.fizz_buzz import FizzBuzz
import unittest


class TestFizBuzz(unittest.TestCase):
    def test_generate_withoutArgs_returns100LongList(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual(100, len(result))

    def test_generate_firstElement_isOneAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("1", result[0])

    def test_generate_divisibleByThree_isFizzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("Fizz", result[2])

    def test_generate_divisibleByFive_isBuzzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("Buzz", result[4])

    def test_generate_devisibleByThreeAndFive_isFizzBuzzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("FizzBuzz", result[14])

    def test_generate_containsThreeButNotDivisibleByIt_isFizzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("Fizz", result[12])

    def test_generate_containsFiveButNotDivisibleByIt_isBuzzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("Buzz", result[51])

    def test_generate_containsThreeAndFiveButNotDivisibleByThem_isFizzBuzzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("FizzBuzz", result[52])

    def test_generate_startWithThreeButNotDisibleByIt_isFizzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("Fizz", result[33])

    def test_generate_containsFiveAndDivisibleByThree_isFizzBuzzAsString(self):
        fb = FizzBuzz()
        result = fb.generate()
        self.assertEqual("FizzBuzz", result[50])


if __name__ == '__main__':
    unittest.main()
